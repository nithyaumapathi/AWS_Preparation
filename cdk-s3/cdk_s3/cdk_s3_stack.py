from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class CdkS3Stack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        s3.Bucket(
            self,
            "MyBucket",
            bucket_name="nithya-cdk-bucket-12345"
        )