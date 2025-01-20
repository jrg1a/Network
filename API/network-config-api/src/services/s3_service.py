import boto3
from botocore.exceptions import NoCredentialsError

class S3Service:
    def __init__(self, bucket_name, aws_access_key, aws_secret_key):
        self.bucket_name = bucket_name
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

    def upload_file(self, file_name, object_name=None):
        if object_name is None:
            object_name = file_name
        try:
            self.s3.upload_file(file_name, self.bucket_name, object_name)
            return True
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def download_file(self, object_name, file_name):
        try:
            self.s3.download_file(self.bucket_name, object_name, file_name)
            return True
        except NoCredentialsError:
            print("Credentials not available")
            return False