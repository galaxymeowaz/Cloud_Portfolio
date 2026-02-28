# 🤖 Automatic Accountant (Serverless Ledger Sync)

Automated bidirectional data synchronization pipeline built entirely on **AWS Free Tier Serverless Infrastructure** (Terraform).

This project integrates Google Calendar and Google Sheets into an event-driven AWS architecture to track client meetings and calculate billing ledgers.

![Architecture Flow](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/AWS_Lambda_logo.svg/150px-AWS_Lambda_logo.svg.png) *(Consider adding an architecture diagram here!)*

## 🏗️ Architecture Design (FinOps Aligned)

This infrastructure is intentionally designed using the **Principle of Least Privilege** and strictly aligns with **Zero-Cost AWS Free Tier** operations:

1. **Daily Ledger Sync (AWS EventBridge -> Lambda)**
   - EventBridge runs a cron schedule `rate(1 day)`
   - Triggers the `ledger_sync` Docker container via AWS Lambda.
   - Authorized via a strict IAM role, it scrapes the previous 24 hours of Google Calendar data.
   - Computes amount owed dynamically using Regex to parse the event title (e.g., `Client Name [$250]`), gracefully falling back to the `HOURLY_RATE` environment variable if none is provided.
   - Appends a new formatted row to Google Sheets via `gspread`, tagging it as `UNPAID`.
   - **FinOps Win:** Bypasses X-Ray Tracing and utilizes minimal memory sizes.



3. **Immutable Artifacts (AWS ECR)**
   - The Lambda functions utilize a shared Docker container deployed in Elastic Container Registry (ECR).
   - **FinOps Win:** Utilizes an ECR Lifecycle Policy to delete old images (max 3), avoiding any storage costs.

---

## 🔒 Security Best Practices Implemented

- **Zero-Trust Secrets Management:** All `.env` files and `credentials.json` are strictly `.gitignore`'d.
- **IAM Scoping:** Lambdas run with the absolute minimum `AWSLambdaBasicExecutionRole`.
- **Infrastructure as Code (IaC):** Explicitly validated by `tfsec` (Aqua Security). Strategic `tfsec:ignore` annotations define acknowledged financial overrides (KMS keys, X-Ray) for Free Tier compliance.
- **Immutable Tags:** Docker images enforce `IMMUTABLE` pushing to guarantee an audit trail.

---

## 🚀 Setup & Deployment
*Note: Due to security, the `credentials.json` required to access the Google APIs must be supplied dynamically by the administrator.*

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/automatic-accountant.git
   cd automatic-accountant
   ```

2. **Supply Google Service Account Credentials:**
   Place your Google Workspace `credentials.json` into the root directory.

3. **Local Testing (Docker Compose):**
   Use the provided bash script to test the Lambda containers locally without deploying to AWS.
   ```bash
   chmod +x test_locally.sh
   ./test_locally.sh
   ```

4. **Deploy Infrastructure (Terraform):**
   *Ensure you have authorized AWS CLI locally.*
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

## 🛠️ Tech Stack
- **Cloud:** AWS (Lambda, EventBridge, IAM, ECR, Cloudwatch)
- **IaC & Security:** Terraform, tfsec
- **Language/Env:** Python 3.9, Docker
- **APIs:** Google Calendar REST, Google Sheets API (`gspread`)
