#import boto3 
import boto3
import json
import os
import glob

# Let's use Amazon S3
s3 = boto3.resource('s3')

# #creating s3 bucket
print("Listing Amazon s3 Create_Bucket" )
bucket = s3.create_bucket(Bucket= 's3boto3s3bucket')
print(f'--{bucket.name}')

# list bucketss
print("Listing Amazon S3 Buckets:")
for bucket in s3.buckets.all():
    print(f'--{bucket.name}')

#uploading object in s3
s3.Bucket('s3boto3s3bucket').upload_file('C:\\Users\devsh\s3-boto3\data\dev1.jpg', 'dev1.jpg')
print("object has uploaded")

# # Listing Amazon S3 Bucket objects/files
s3_bucket = s3.Bucket('s3boto3s3bucket')
print('Listing Amazon S3 Bucket objects/files:')
for obj in s3_bucket.objects.all():
    print(f'-- {obj.key}')

# # Download object form s3 bucket
# s3_object = s3.Object('s3boto3s3bucket', 'dev1.jpg')
# s3_object.download_file('dev1.jpg')
# print('S3 object download complete')

# #delete object
s3.Object('s3boto3s3bucket', 'dev1.jpg').delete()
print('object has deleted')

# #delete bucket()
bucket.delete()
print('bucket has deleted')

# s3 = boto3.client("s3")
# cwd=os.getcwd()
# cwd=cwd+"/data/"
# files = glob.glob(cwd+"*.jpg")
# for file in files:
#     s3.upload_file(
#     Filename = file,
#     Bucket = "s3boto3s3bucket",
#     Key = file.split("/")[-1])