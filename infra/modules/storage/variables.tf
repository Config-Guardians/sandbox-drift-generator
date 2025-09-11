# Variables to store passed values from parent module

variable "project_prefix" {
  description = "Prefix for all resources"
  type        = string
  # Validate that the prefix is alphanumeric and between 3 and 30 characters and no capitals
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

variable "test_force_destroy" {
  description = "Whether to force destroy the test bucket"
  type        = bool
  default     = false
}