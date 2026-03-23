import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

print("Total buckets:", len(response['Buckets']))

for bucket in response['Buckets']:
    print("Bucket Name:", bucket['Name'])