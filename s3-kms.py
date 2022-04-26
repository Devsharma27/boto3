#import boto3 
import boto3
import json

# Let's use Amazon S3
s3 = boto3.resource('s3')

#creating s3 bucket
print("Listing Amazon s3 Create_Bucket" )
bucket = s3.create_bucket(Bucket= 's3boto3s3bucket')
print(f'--{bucket.name}')

s3 = boto3.client('s3')

bucket_policy = {
  "Version": "2012-10-17",
  "Id": "PutObjectPolicy",
  "Statement": [
    {
      "Sid": "DenyIncorrectEncryptionHeader",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::s3boto3s3bucket/*",
       "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms",
          "s3:x-amz-server-side-encryption-aws-kms-key-id": "arn:aws:kms:us-east-1:128680359488:key/377b66ca-1346-44e9-a7f3-dfc9840fbbdb"
        }
      }
    },
    {
      "Sid": "DenyUnencryptedObjectUploads",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::s3boto3s3bucket/*",
      "Condition": {
        "Null": {
          "s3:x-amz-server-side-encryption": "true",
          "s3:x-amz-server-side-encryption-aws-kms-key-id": "arn:aws:kms:us-east-1:128680359488:key/377b66ca-1346-44e9-a7f3-dfc9840fbbdb"
        }
      }
    }
  ]
}

bucket_policy = json.dumps(bucket_policy)
s3.put_bucket_policy(Bucket='s3boto3s3bucket', Policy=bucket_policy)
