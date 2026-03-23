import boto3

s3 = boto3.client('s3')

bucket_name = "nithya-python-bucket-12345"

files = ["file1.txt", "file2.txt"]

for file in files:
    s3.upload_file(file, bucket_name, file)
    print(f"{file} uploaded successfully!")

print("All files uploaded!")