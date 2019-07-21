import os 
import sys 

import boto3 ## Package to connect to AWS Services using python


class s3:

    def __init__(self, AWS_KEY, AWS_SECRET):
        """
        Initialized by connecting to AWS User
        arguments =
        1. AWS_Key = User Key Credential (IAM)
        2. AWS_Secret = User Key Secret (IAM)
        """
        self.aws_key = AWS_KEY 
        self.aws_secret = AWS_SECRET 
        self.user = boto3.client(   's3', 
                                    aws_access_key_id=self.aws_key , 
                                    aws_secret_access_key = self.aws_secret
                                    )

    def create_bucket(self, bucket):
    """
    Method to create Bucket to S3:
    class.create_bucket(bucket)
    bucket = Name of the bucket you want to specify
    """
        return self.user.create_bucket(bucket)

    def list_buckets(self):
    """
    Def : List all the bucket in S3
    class.list_buckets()

    return list of buckets in your S3 account
    """
        return self.user.list_buckets()

    def list_objects(self, bucket):
    """
    Def : list all objects in your bucket 
    class.list_objects(bucket)

    bucket = bucket name (object place holder) that you want to retrieve

    return dictionary of object list
    """
        return self.user.list_objects(Bucket=bucket)

    def upload_file(self, bucket, filename, key):
    """
    Def : upload file to S3
    class.upload_file(bucket, filename, key)
    bucket = Bucket name directory in your S3
    filename = local path directory that you want to upload
    key = name file that you want to save
    """
        self.user.upload_file(  Filename=filename , 
                                Bucket=bucket , 
                                Key=key
                                ) 

    def download_file(self, bucket, filename, key):
    """
    Def : Download file from S3 using IAM credential
    class.download_file(bucket, filename, key)
    
    bucket = Bucket name directory in your S3
    filename = local path directory that you want to upload
    key = name file that you want to save

    return file that you downloaded
    """
        self.user.download_file(Filename = filename ,
                                Bucket = bucket ,
                                Key = key
        )


