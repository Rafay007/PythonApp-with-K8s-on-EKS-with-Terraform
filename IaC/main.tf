terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
  backend "s3" {
    bucket = "aisight"
    key    = "aisight-terraform-state/state.tfstate"
    region = "eu-central-1"
  }
}
