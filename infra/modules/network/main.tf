# Create a secure security group with no inbound rules for drift application:

# Automatically get the default VPC
data "aws_vpc" "default" {
  default = true
}

resource "aws_security_group" "sandbox_sg" {
    name = "${var.project_prefix}-sandbox-sg"
    vpc_id = coalesce(var.vpc_id, data.aws_vpc.default.id)

    # Outbound: allow all by default
    egress {
        description = "Allow all traffic outbound by default"
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }

    # Ingress: deny all by default

    tags = merge(
        var.tags,
        {
        Name = "${var.project_prefix}-sandbox-sg"
        }
    )
}