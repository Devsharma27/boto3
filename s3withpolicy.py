#import boto3 
import boto3
import json

# Let's use Amazon S3
s3 = boto3.resource('s3')

#creating s3 bucket
print("Listing Amazon s3 Create_Bucket" )
bucket = s3.create_bucket(
    Bucket= 's3boto3s3bucket',
    ACL = 'private')
print(f'--{bucket.name}')

s3 = boto3.client('s3')

bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:DeleteObject",
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::s3boto3s3bucket/*"
        },
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::s3boto3s3bucket"
        }
    ]
}

bucket_policy = json.dumps(bucket_policy)
s3.put_bucket_policy(Bucket='s3boto3s3bucket', Policy=bucket_policy)

response= s3.put_public_access_block(
        Bucket='s3boto3s3bucket',
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        },
    )

data = open('C:\\Users\devsh\s3-boto3\data\dev1.jpg', 'rb')
s3.put_object(
    Bucket= 's3boto3s3bucket',
    Key='dev1.jpg',
    Body=data,
    ACL = 'private',
    ServerSideEncryption='aws:kms',
    )
print("object has uploaded")


# #delete object
# s3.Object('s3boto3s3bucket', 'dev1.jpg').delete()
# print('object has deleted')

# #delete bucket()
# bucket.delete()
# print('bucket has deleted')