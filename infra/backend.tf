# To connect to the remote state of the infrastructure (Lock-Table and State-Bucket)
# terraform {
#   backend "s3" {
#     bucket         = "fyp-terraform-state-bucket"   # from bootstrap output
#     key            = "infra/terraform.tfstate"       # path/key inside the bucket
#     region         = "ap-southeast-1"                # same region as the bucket
#     dynamodb_table = "fyp-terraform-lock-table"      # from bootstrap output
#     encrypt        = true
#   }
# }

# If names are different.. needa input commands as follows

# Code would change to:
## terraform { backend "s3" {} }

# Then run the command below to reconfigure the backend
## terraform init \
##  -backend-config="bucket=fyp-terraform-state-bucket" \
##  -backend-config="key=infra/terraform.tfstate" \
##  -backend-config="region=ap-southeast-1" \
##  -backend-config="dynamodb_table=fyp-terraform-lock-table" \
##  -backend-config="encrypt=true" \
##  -reconfigure