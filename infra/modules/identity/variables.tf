variable "project_prefix" {
    description = "Prefix for all resources"
    type = string
    validation {
        condition     = can(regex("^[a-z0-9-]{3,30}$", var.project_prefix))
        error_message = "project_prefix must be 3–30 chars, lowercase letters, digits, or hyphens."
    }
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}

variable "test_bucket_arn" {
    description = "ARN of the bucket that we give access to for sandbox-user"
    type = string
}