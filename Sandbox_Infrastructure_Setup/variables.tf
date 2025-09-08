# This file is used to define the variables that can be used throughout the Terraform configuration
# AWS Region
variable "region" {
    description = "The AWS region being used for this project"
    type        = string
    default     = "ap-southeast-1"
}

# S3 Bucket Name
variable "s3_bucket_name" {
    description = "Name of demo S3 bucket"
    type        = string
}