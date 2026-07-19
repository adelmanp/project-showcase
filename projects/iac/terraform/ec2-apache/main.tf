resource "aws_instance" "lesson_06" {
  ami                         = var.ami_id
  instance_type               = var.instance_type
  key_name                    = aws_key_pair.deployer.key_name
  associate_public_ip_address = true

  vpc_security_group_ids = [
    aws_security_group.sg_ssh.id,
    aws_security_group.sg_http.id,
  ]

  user_data = templatefile("${path.module}/scripts/apache-mkdocs.yaml.tftpl", {
    public_key = var.public_key
  })

  tags = {
    Name = "Lesson_06-Cloud-Init"
  }
}

resource "aws_key_pair" "deployer" {
  key_name   = var.key_name
  public_key = var.public_key
}

resource "aws_security_group" "sg_ssh" {
  name        = "${var.project_name}-ssh"
  description = "Allow SSH access to the EC2 instance"

  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    protocol    = "tcp"
    from_port   = 22
    to_port     = 22
  }

  egress {
    cidr_blocks = ["0.0.0.0/0"]
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
  }
}

resource "aws_security_group" "sg_http" {
  name        = "${var.project_name}-http"
  description = "Allow HTTP access to the Apache web server"

  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    protocol    = "tcp"
    from_port   = 80
    to_port     = 80
  }

  egress {
    cidr_blocks = ["0.0.0.0/0"]
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
  }
}
