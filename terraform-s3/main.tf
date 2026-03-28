provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "nithya-terraform-bucket-12345"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "nithya-terraform-bucket-12345"

  versioning {
    enabled = true
  }
}