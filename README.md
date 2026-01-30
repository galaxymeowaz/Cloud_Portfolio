# Joseph's Cloud Portfolio:

A technical log of my journey mastering **AWS (Amazon Web Services)**, **Linux (Ubuntu via WSL2)** and **Cloud Architecture**.

All learning documentation is written in **Visual Studio Code (VSC)** and is uploaded directly to **GitHub**. 

## Deployment Pipeline 
This project uses a **CI/CD pipeline** via GitHub Actions.
- **Trigger** Push to `main` branch.
- **Runner:** `ubuntu-latest`.
- **Steps:**
 1. Checkout code.
 2. Configure AWS Credentials (via GitHub Secrets)
 3. Sync files to AWS S3
 4. Invalidate AWS CloudFront Cache.