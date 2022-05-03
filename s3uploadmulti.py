import boto3
import os
import glob

# Let's use Amazon S3
s3 = boto3.client("s3")
s3.create_bucket(Bucket = "s3boto3s3bucket")

cwd=os.getcwd()
cwd=cwd+"/data/"
files = glob.glob(cwd+"*.jpg")
for file in files:
    s3.upload_file(
    Filename = file,
    Bucket = "s3boto3s3bucket",
    Key = file.split("/")[-1])




