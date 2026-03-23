import boto3

s3 = boto3.client('s3')

bucket_name = "nithya-python-bucket-12345"

# Delete all objects first
objects = s3.list_objects_v2(Bucket=bucket_name)

if 'Contents' in objects:
    for obj in objects['Contents']:
        s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

# Now delete bucket
s3.delete_bucket(Bucket=bucket_name)

print(f"Bucket '{bucket_name}' deleted successfully!")