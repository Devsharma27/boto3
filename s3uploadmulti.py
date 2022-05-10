import boto3
import os
import glob

# Let's use Amazon S3
s3 = boto3.client("s3")
bucket = s3.create_bucket(Bucket = "s3boto3s3bucket")

cwd=os.getcwd()
cwd=cwd+"/data/"
files = glob.glob(cwd+"*.jpg")
for file in files:
    s3.upload_file(
    Filename = file,
    Bucket = "s3boto3s3bucket",
    Key = file.split("/")[-1]
    )
cwd=cwd+"/data1/"
files = glob.glob(cwd+"*.jpg")
for file in files:
    s3.upload_file(
    Filename = file,
    Bucket = "s3boto3s3bucket",
    Key = file.split("/")[-1]
    )


response = s3.list_buckets()
print("Listing Amazon S3 Buckets:")
for bucket in response['Buckets']:
    print(f"-- {bucket['Name']}")
    
print("listing objects")
objects = s3.list_objects_v2(Bucket='s3boto3s3bucket')
for obj in objects['Contents']:
    print("object:",obj['Key'])





