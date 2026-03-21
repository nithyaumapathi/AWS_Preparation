# Create S3 Bucket

## 📌 Description
This command is used to create a new S3 bucket in AWS.

## 🧾 Command

aws s3 mb s3://nithya-aws-preparation-2026

## 🌍 Region-specific command

aws s3api create-bucket \
--bucket nithya-aws-preparation-2026-germany \
--region ap-south-1 \
--create-bucket-configuration LocationConstraint=ap-south-1

## 📋 Explanation

- aws s3 mb → make bucket
- s3://bucket-name → unique bucket name
- region → specifies AWS region (Mumbai = ap-south-1)

## ⚠️ Important Notes

- Bucket name must be globally unique
- Use lowercase letters only
- No spaces allowed

## ✅ Verification

To check if bucket is created:

aws s3 ls