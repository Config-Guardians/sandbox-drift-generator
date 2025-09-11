# Variables for infrastructure main module

# Region
variable "region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "ap-southeast-1"
}

# Profile
variable "profile" {
  description = "AWS profile to use"
  type        = string
  default     = "FYP"
}

# Project-Prefix
variable "project_prefix" {
    description = "Prefix for all resources"
    type        = string
    default     = "fyp"
}

# Environment
variable "environment" {
  description = "Environment name for tagging (dev, ci, prod)"
  type        = string
  default     = "dev"
}