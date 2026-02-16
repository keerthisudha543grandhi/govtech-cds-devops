############################################
# Terraform Remote Backend (S3 + DynamoDB)
############################################
terraform {
  backend "s3" {
    bucket         = "visitor-eks-terraform-state"
    key            = "eks/terraform.tfstate"
    region         = "ap-southeast-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
