# Variables for bootstrap
variable "region" {
    description = "The AWS region to deploy resources in"
    type        = string
    default     = "ap-southeast-1"
}

variable "profile" {
    description = "The AWS CLI profile to use"
    type        = string
    default     = "FYP"
}

# Resource names
variable "state_bucket_name" {
    description = "The name of the S3 bucket for Terraform state"
    type        = string
    default     = "fyp-terraform-state-bucket"
}

variable "lock_table_name" {
    description = "The name of the DynamoDB table for state locking"
    type        = string
    default     = "fyp-terraform-lock-table"
}