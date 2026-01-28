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