#!/bin/bash

echo "Listing existing buckets..."
aws s3 ls

echo "Creating new bucket..."
aws s3 mb s3://nithya-aws-script-2026-1234

echo "Listing buckets after creation..."
aws s3 ls