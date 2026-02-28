# Automatic Accountant: Ultimate Setup Guide
> *Created by Joseph Tay (aztay.org) | Copyright (c) 2026 | Licensed under the MIT License.*

This comprehensive guide serves as a manual for setting up the **Automatic Accountant** pipeline from scratch. When you are ready to transition from a dummy test account to your actual business accounts, follow these steps sequentially to create the required Cloud APIs, connect the environment variables, and deploy your infrastructure to AWS.

## 🛠️ Prerequisites
Before starting, ensure your computer has the following tools installed:
1.  **[Python 3.9+](https://www.python.org/downloads/):** The programming language that runs the logic.
2.  **[Docker](https://www.docker.com/products/docker-desktop/):** Packages the code so it runs identically on your laptop and the cloud.
3.  **[Terraform](https://developer.hashicorp.com/terraform/downloads):** An "Infrastructure as Code" tool that automatically builds the cloud servers for you by reading the `main.tf` file.
4.  **[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html):** Allows your laptop terminal to securely talk to Amazon Web Services.
5.  **Git/VSCode:** To edit your code and `.env` files easily.

---

## 📌 Phase 1: Google Cloud Platform (GCP) Setup
We need to give our script legal permission to read your Google Calendar and edit your Google Sheets. Instead of using your personal Gmail password, we will create a secure "Robot User" (a Service Account) in Google Cloud Platform (GCP).

### Step 1.1: Create a Google Cloud Project
1. Log into the [Google Cloud Console](https://console.cloud.google.com).
2. Click the **Project Dropdown** at the top left of the screen and click **New Project**.
3. Name it `Automatic Accountant` and click **Create**. Ensure it is selected.

### Step 1.2: Enable the APIs
1. On the left sidebar menu, click **APIs & Services > Library**.
2. Search for **Google Calendar API**, click it, and hit the blue **Enable** button.
3. Search again for **Google Sheets API**, click it, and hit **Enable**.

### Step 1.3: Generate the Service Account Robot
1. On the left menu, go to **APIs & Services > Credentials**.
2. Click **+ CREATE CREDENTIALS** at the top and select **Service account**.
3. Name it "Billing Robot" and click **Create and Continue**.
4. In the "Role" dropdown (Step 2), select **Basic > Editor** and click **Done**.
5. Once created, you will see it listed under Service Accounts. It has an email address that looks like `billing-robot@automatic-accountant-....iam.gserviceaccount.com`. **Copy that robot email address.**

### Step 1.4: Download the `credentials.json` File
1. Under "Service Accounts", click the pencil icon or the email address of the robot you just made.
2. Go to the **KEYS** tab at the top.
3. Click **ADD KEY > Create new key**.
4. Select **JSON** and hit **Create**. A file will immediately download to your computer.
5. Move that downloaded file directly into your `automatic-accountant` folder on your laptop and rename the file simply to `credentials.json`. 

---

## 📌 Phase 2: Connecting the Google Calendars and Sheets

### Step 2.1: Authorize the Robot
Google keeps everything private by default. The robot cannot see your calendar unless you explicitly invite it.
1. Open up your real business Google Calendar.
2. Find the specific Calendar you want to use on the left sidebar. Click `⋮` next to the name, then **Settings and sharing**.
3. Scroll down to "Share with specific people or groups" and click **Add People and Groups**.
4. Paste the robot's email address you copied in Step 1.3, give it permissions to "See all event details", and click Send.
5. **DO THE EXACT SAME THING FOR YOUR SPREADSHEET:** Open the Google Sheet where you want the bills deposited, click the green "Share" button at the top right, and invite the robot's email as an "Editor".

### Step 2.2: Fetch Your Specific IDs
You now need to tell the Python script *which* calendar and sheet to look at.
1. **Calendar ID:** Still on the Calendar "Settings and sharing" page, scroll down to "Integrate Calendar". Copy the `Calendar ID` (e.g., `c_1a2b3c...@group.calendar.google.com`).
2. **Spreadsheet ID:** Look at the URL of your Google Sheet. It looks like `https://docs.google.com/spreadsheets/d/1BxiMVs0X.../edit`. The ID is the random string inside the slashes: `1BxiMVs0X...`

### Step 2.3: Correctly Format Your Google Sheet
For the Robot to automatically deposit rows into your spreadsheet, it needs a specific header structure on Row 1.
1. Open your Google Sheet.
2. In the very first row (A1 to G1), type exactly these headers:
    - **A1:** `Event Date`
    - **B1:** `Client`
    - **C1:** `Service`
    - **D1:** `Amount Owed`
    - **E1:** `Status`
    - **F1:** `Payment Received Date`
    - **G1:** `Comments (Manual Entry)`

### Step 2.4: Correctly Format Your Calendar Events
When scheduling a meeting with a client, the Robot looks at the **Event Title** to calculate money and services.
*   **Format:** `Client Name [$Rate] - Service Type`
*   **Example:** `Wayne Enterprises [$250] - Architecture Review`

**Rules to Remember:**
1.  **Dynamic Rates:** If you want to charge a specific hourly rate, put it anywhere in the title using brackets, parentheses, or a $ sign (e.g., `[$250]`, `($150)`, `$90.50`). If you leave it out, the Robot defaults to the `HOURLY_RATE` variable in your `.env` file.
2.  **Service Type:** If you want to specify a service, put a hyphen `-` followed by the service name. If you leave it out, the Robot defaults to `Consulting / Meeting`.
3.  **Times are Required:** You **cannot** use the "All-Day" checkbox. The Event must have a specific Start Time and End Time (e.g., `1:00 PM - 3:00 PM`) so the Robot can calculate the duration multiplied by the rate!

---

## 📌 Phase 3: Amazon Web Services (AWS) Setup
AWS is where the code executes daily. To do this securely, we will create an **IAM (Identity and Access Management)** User. This creates a strict "Least Privilege" security guard so your laptop can run Terraform without accidentally giving it the keys to your entire Amazon account.

### Step 3.1: Create the Setup Policy
1. Log into your AWS Console and search for **IAM**.
2. Go to **Policies** (left menu) > **Create policy**.
3. Select the **JSON** tab and paste the Custom Terraform Policy code below. This code uses "Least Privilege"—it only grants the exact permissions Terraform needs to build this specific project and nothing else:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowIAMRoleCreation",
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:GetRole",
                "iam:PassRole",
                "iam:PutRolePolicy",
                "iam:DeleteRolePolicy",
                "iam:GetRolePolicy",
                "iam:ListRolePolicies",
                "iam:ListInstanceProfilesForRole",
                "iam:ListAttachedRolePolicies",
                "iam:AttachRolePolicy",
                "iam:DetachRolePolicy",
                "iam:TagRole"
            ],
            "Resource": "arn:aws:iam::*:role/automatic_accountant_role"
        },
        {
            "Sid": "AllowLambdaManagement",
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:GetFunctionConfiguration",
                "lambda:UpdateFunctionConfiguration",
                "lambda:UpdateFunctionCode",
                "lambda:ListTags",
                "lambda:TagResource",
                "lambda:AddPermission",
                "lambda:RemovePermission",
                "lambda:GetPolicy",
                "lambda:ListVersionsByFunction"
            ],
            "Resource": "arn:aws:lambda:*:*:function:ledger_sync_function"
        },
        {
            "Sid": "AllowECRManagement",
            "Effect": "Allow",
            "Action": [
                "ecr:CreateRepository",
                "ecr:DeleteRepository",
                "ecr:DescribeRepositories",
                "ecr:PutLifecyclePolicy",
                "ecr:GetLifecyclePolicy",
                "ecr:DeleteLifecyclePolicy",
                "ecr:ListTagsForResource",
                "ecr:TagResource",
                "ecr:GetAuthorizationToken",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage",
                "ecr:ListImages",
                "ecr:DescribeImages",
                "ecr:BatchGetImage"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowEventBridgeManagement",
            "Effect": "Allow",
            "Action": [
                "events:PutRule",
                "events:DeleteRule",
                "events:DescribeRule",
                "events:EnableRule",
                "events:DisableRule",
                "events:PutTargets",
                "events:RemoveTargets",
                "events:ListTargetsByRule",
                "events:ListTagsForResource",
                "events:TagResource"
            ],
            "Resource": "arn:aws:events:*:*:rule/daily_ledger_sync_rule"
        }
    ]
}
```

4. Click Next, name it `AutomaticAccountant-TerraformDeployer`, and hit Create.

### Step 3.2: Create the IAM User & Access Keys
1. In IAM, go to **Users** > **Create user**.
2. Name it `terraform-admin`. Do *not* give them AWS Management Console access. Wait to attach policies manually.
3. Select **Attach policies directly**, search for `AutomaticAccountant-TerraformDeployer`, check it, and create the user.
4. Click on the user `terraform-admin` > **Security credentials** tab.
5. Under "Access keys", click **Create access key** ->  **Command Line Interface (CLI)**.
6. A window will pop up with an **Access Key ID** and **Secret Access Key**. *Copy both of these immediately!* They will vanish forever if you close the window.

---

## 📌 Phase 4: Setting the Environment Variables
You now have all the puzzle pieces. It's time to put them into the `.env` file on your laptop so your script knows where to look.

1. Ensure you have copied `.env.example` to a new file named `.env`.
2. Inside your `.env` file, paste everything you discovered:

```text
GOOGLE_SHEETS_SPREADSHEET_ID=1BxiMVs0X_xxxxxxxxxxxxxxxxxxx
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=skJhg...
HOURLY_RATE=150
CALENDAR_ID=c_xyz123@group.calendar.google.com
SYNC_DAYS_BACK=1
```

*(Note: Use `SYNC_DAYS_BACK=30` for a one-time historical backfill test. Once completed, change it to `1` so AWS only scans for yesterday's meetings daily to prevent 30-day infinite duplicates!)*

---

## 📌 Phase 5: Testing & Deployment

### Step 5.1: Test Locally via Docker
Before deploying to the cloud, prove that the math and permissions work locally. Make sure you've scheduled a dummy meeting on the calendar first!
```bash
./test_locally.sh
```
If your Google Sheet populates perfectly, you are ready for AWS.

### Step 5.2: Launch the Infrastructure
Use Terraform to dynamically build the AWS Architecture (Storage, IAM Roles, Cron Jobs, Lambda containers). Instead of clicking buttons on the AWS website, Terraform reads `main.tf` to build everything safely.
```bash
terraform init
terraform plan
terraform apply
```
*Note: Type `yes` when prompted. When it finishes, Terraform will output an `ecr_repository_url` in green text. Copy that URL!*

### Step 5.3: Upload the Brain to AWS
You built the empty Lambda server in Step 5.2. Now, you must bundle your Python code with the Google dependencies into a Docker container and push it to **AWS ECR (Elastic Container Registry)**. ECR is essentially a private cloud folder where AWS stores your Docker images securely.

*Note: You must have the AWS CLI installed and configured on your laptop (`aws configure`) using the Access Keys you generated in Step 3.2.*
```bash
# 1. Login your laptop's Docker engine to AWS AWS
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin YOUR_AWS_ACCOUNT_ID.dkr.ecr.ap-southeast-1.amazonaws.com

# 2. Build the Docker Image for AWS (Forcing x86 Architecture and disabling OCI Provenance)
docker build --platform linux/amd64 --provenance=false -t automatic-accountant-repo .

# 3. Tag it for the ECR URL you copied in Step 5.2
docker tag automatic-accountant-repo:latest YOUR_ECR_REPO_URL:v6

# 4. Push the physical code to AWS
docker push YOUR_ECR_REPO_URL:v6
```

**Congratulations!** AWS EventBridge will now trigger the AWS Lambda every 24 hours to automatically calculate your bills. Nothing more for you to click or touch.
