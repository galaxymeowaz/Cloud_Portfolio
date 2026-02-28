# AWS Architecture Notes

## 1. VPC Networking 

Public Subnet: ### Public Subnet -> Web Serer (Lobby)
Private Subnet: ### Private Subnet -> Database (Vault) 

Public Subnet is meant for the public to see (such as websites)
Private Subnets: 

Best practice is to have at least 3 different types of subnets. 

First is public, second is private and third is data. 

Public subnets usually contain bastion/jumphosts, NAT Gateway, and public load balancers. Private subnets contain web servers, application servers. 

Data subnets usually contain databases and file sharing servers (Netapp Ontap, FSX/Windows file share). 

Both private and data subnets are technically the same thing, but should supposed to be logically separate. 

## 2. Notes about Terraform, IAM and AWS Lambda. 

I originally created an IAM User for my Automatic Accountant project (Terraform.tf) to have Full Admin Access, but I decided to change it as that is not following the principles of "least privilege". I therefore starting doing research on how to start creating secure JSON Policies and my notes regarding it are as follows: 

'Effect' means is something allowed to do something. By default, AWS doesn't allow anything (Implicit Deny) so we normally write "Effect": "Allow" to enable a user to do something

'Action' is basically a verb for what the user can or can't do. For example enabling Lambda etc. "lambda:CreateFunction" (it can create new lambda), "lambda:DeleteFunction" 

'Resource' is used to tell the jSON policy exactly what they are allowed to do? (Eg: "Resource": "arn:aws:lambda:*:*:function:ledger_sync_function")

This translates to English as: "Terraform is only allowed to edit/delete Lambda functions specifically named ledger_sync_function."

If a hacker manages to steal my Terraform login keys and tries to delete one of my other secret AWS web servers, AWS will read this JSON file, see that the server is not named ledger_sync_function, and instantly block the hacker from deleting it. That is the magic of strict JSON policies!

"Resource": "arn:aws:lambda:*:*:function:ledger_sync_function"

"arn" is always the starting prefix of Amazon Resource Names (ARN)

"aws" is the partition used by default unless we are using AWS China or AWS GovCloud.

"lambda" is the AWS service I am trying to use.

"*" the first "*" that appears above is to the wildcard meaning "any region". If I want to lock it down to a specific AWS region such as Singapore, it should be replaced with "ap-southeast-1"

"*" the second "*" that appears is a wildcard representing "any account". This is dangerous in an actual production environment, it should be replaced with my 12 digit AWS Account ID to prevent cross account issues.

"function:ledger_sync_function" "function" is the resource type followed by the exact name of my resource "ledger_sync_function" 
++++
AWS Lambda is an event-driven, serverless compute service. Meaning it automatically runs code on a specific trigger (eg: When it is 12pm every day, or when I upload an S3 file) I will not need to provision or manage any servers. I only pay for the exact seconds that my code runs. (time-based triggers in AWS are managed by a service called "Amazon EventBridge) 

Terraform is used to define and deploy cloud resources such as EC2, S3's etc. It is an Infrastructure as Code (IaC) tool which is used to deploy and update cloud resources. It is "cloud-agnostic" meaning it works with AWS, Azure and Google Cloud,