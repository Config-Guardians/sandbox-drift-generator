variable "project_prefix" {
    description = "Prefix for all resource"
    type = string 
    validation {
        condition = can(regex("^[a-z0-9-]{3,30}$", var.project_prefix))
        error_message = "project_prefix must be 3–30 chars, lowercase letters, digits, or hyphens."
    }
}

variable "vpc_id" {
    description = "VPC ID to associate the security group with (Optional since I'm already using default)"
    type = string
    default = null
}

variable "tags" {
  description = "Common tags"
  type = map(string)
  default = {}
}