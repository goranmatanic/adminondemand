terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.20.0"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "2.77.0"

  name                 = "admin-demand-vpc"
  cidr                 = "10.0.0.0/16"
  azs                  = ["eu-central-1a", "eu-central-1b"]
  public_subnets       = ["10.0.0.0/24", "10.0.1.0/24"]
  enable_dns_hostnames = true
  enable_dns_support   = true
}

resource "aws_db_subnet_group" "admin-demand-db-group" {
  name       = "admin-demand-db-group"
  subnet_ids = module.vpc.public_subnets

  tags = {
    "Name" = "admin-demand-db-group"
  }
}

resource "aws_security_group" "rds" {
  name   = "rds-security-group"
  vpc_id = module.vpc.vpc_id

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "rds-security-group"
  }
}

resource "aws_db_instance" "admin-demand-db" {
  identifier             = "admin-demand-db"
  instance_class         = "db.t2.micro"
  allocated_storage      = 20
  engine                 = "mysql"
  engine_version         = "8.0.28"
  username               = var.db_username
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.admin-demand-db-group.name
  vpc_security_group_ids = [aws_security_group.rds.id]
  publicly_accessible    = true
  skip_final_snapshot    = true
}
