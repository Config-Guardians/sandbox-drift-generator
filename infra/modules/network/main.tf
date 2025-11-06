# Create a secure security group with no inbound rules for drift application:

# Automatically get the default VPC
data "aws_vpc" "default" {
  default = true
}

resource "aws_security_group" "sandbox_sg" {
    name = "${var.project_prefix}-sandbox-sg"
    vpc_id = coalesce(var.vpc_id, data.aws_vpc.default.id)

    # Outbound: restrict only to internal VPC
    egress {
        description = "Allow only VPC-internal traffic"
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = [data.aws_vpc.default.cidr_block]
    }

    # Ingress: deny all by default

    tags = merge(
        var.tags,
        {
        Name = "${var.project_prefix}-sandbox-sg"
        }
    )
}