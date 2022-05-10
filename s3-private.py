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

#private bucket
s3.put_public_access_block(
    Bucket='s3boto3s3bucket',
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': True,
        'IgnorePublicAcls': True,
        'BlockPublicPolicy': True,
        'RestrictPublicBuckets': True
    },
)
# applying encryption to the object
s3.put_bucket_encryption(
    Bucket= 's3boto3s3bucket', 
    ServerSideEncryptionConfiguration={
        'Rules': [
            {
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'aws:kms',
                    'KMSMasterKeyID': 'arn:aws:kms:us-east-1:128680359488:key/377b66ca-1346-44e9-a7f3-dfc9840fbbdb'
                },
                'BucketKeyEnabled': True
            },
        ]
    },
)

data = open('C:\\Users\devsh\s3-boto3\data\dev2.jpg', 'rb')
s3.put_object(
    Bucket= 's3boto3s3bucket',
    Key='dev2.jpg',
    Body=data,
    ACL = 'private',
    ServerSideEncryption='aws:kms',
    )
print("object has uploaded")

# # delete object
# s3.Object('s3boto3s3bucket', 'dev1.jpg').delete()
# print('object has deleted')

# #delete bucket()
# bucket.delete()
# print('bucket has deleted')