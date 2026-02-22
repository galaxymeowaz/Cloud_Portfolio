variable "aws_region" {
  description = "The AWS region to deploy to"
  default     = "us-east-1"
}

variable "calendar_id" {
  description = "The ID of the Google Calendar (e.g., email address)"
  type        = string
}

variable "sheet_id" {
  description = "The ID of the Google Sheet"
  type        = string
}
