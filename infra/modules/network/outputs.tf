output "sandbox_sg_id" {
    description = "ID of the sandbox security group"
    value = aws_security_group.sandbox_sg.id
}

output "sandbox_sg_name" {
    description = "Name of the sandbox security group"
    value = aws_security_group.sandbox_sg.name
}