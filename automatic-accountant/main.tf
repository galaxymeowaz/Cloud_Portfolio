terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "ap-southeast-1" # Singapore

  # Best Practice: Tagging resources for Cost Allocation
  default_tags {
    tags = {
      Project     = "AutomaticAccountant"
      Environment = "Dev"
      Owner       = "GalaxyMeowAz"
    }
  }
}

# --- ECR Repository (Where we store the Docker Image) ---
# tfsec:ignore:aws-ecr-repository-customer-key Explicitly avoiding KMS Custom Keys to strictly align with AWS Free Tier (FinOps)
resource "aws_ecr_repository" "app_repo" {
  name                 = "automatic-accountant-repo"
  image_tag_mutability = "IMMUTABLE" # Security: Prevents overwriting tags (Audit trail)

  image_scanning_configuration {
    scan_on_push = true # Security: Auto-scan for vulnerabilities
  }

  encryption_configuration {
    encryption_type = "AES256" # Standard free encryption
  }
}

# --- Lifecycle Policy (FinOps: Zero Cost Protection) ---
# Keeps only the last 3 images to ensure we stay under the 500MB Free Tier limit.
resource "aws_ecr_lifecycle_policy" "repo_policy" {
  repository = aws_ecr_repository.app_repo.name

  policy = jsonencode({
    rules = [{
      rulePriority = 1
      description  = "Keep last 3 images"
      selection = {
        tagStatus   = "any"
        countType   = "imageCountMoreThan"
        countNumber = 3
      }
      action = {
        type = "expire"
      }
    }]
  })
}

# --- Outputs ---
# We need this URL to push our Docker image later.
output "ecr_repository_url" {
  value       = aws_ecr_repository.app_repo.repository_url
  description = " The URL of the ECR repository"
}

# --- IAM Role (The Identity) ---
# This allows the Lambda service to assume this role.
resource "aws_iam_role" "lambda_exec" {
  name = "automatic_accountant_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# --- IAM Policy Attachment (The Permissions) ---
# tfsec:ignore:aws-iam-no-policy-wildcards Using managed AWS policy to avoid custom wildcards, acknowledging risk.
# We attach the "Basic Execution" policy so the Lambda can write logs to CloudWatch.
resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# --- Lambda 1: Ledger Sync (Scheduled Worker) ---
# tfsec:ignore:aws-lambda-enable-tracing Explicitly disabling X-Ray Tracing to strictly align with AWS Free Tier
resource "aws_lambda_function" "ledger_sync" {
  function_name = "ledger_sync_function"
  role          = aws_iam_role.lambda_exec.arn
  package_type  = "Image"
  image_uri     = "${aws_ecr_repository.app_repo.repository_url}:v3"
  timeout       = 60
  memory_size   = 128

  environment {
    variables = {
      ENV = "dev"
    }
  }
}

# --- EventBridge Target for Ledger Sync ---
resource "aws_cloudwatch_event_rule" "daily_ledger_sync" {
  name                = "daily_ledger_sync_rule"
  description         = "Trigger Ledger Sync Lambda daily"
  schedule_expression = "rate(1 day)"
}

resource "aws_cloudwatch_event_target" "ledger_sync_target" {
  rule      = aws_cloudwatch_event_rule.daily_ledger_sync.name
  target_id = "LedgerSyncLambdaTarget"
  arn       = aws_lambda_function.ledger_sync.arn
}

resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ledger_sync.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.daily_ledger_sync.arn
}
