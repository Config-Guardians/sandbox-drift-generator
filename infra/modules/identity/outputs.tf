output "sandbox_user_name" {
  description = "IAM sandbox user name"
  value       = aws_iam_user.sandbox_user.name
}