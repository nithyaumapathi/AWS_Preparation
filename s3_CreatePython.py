import boto3

s3 = boto3.client('s3', region_name='ap-south-1')

bucket_name = "nithya-python-bucket-12345"  

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print(f"Bucket '{bucket_name}' created successfully!")