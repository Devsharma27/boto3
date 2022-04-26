# from urllib import response
# import boto3

# ec2 = boto3.resource('ec2', region_name='us-east-1')
# instance = ec2.Instance('id')
# instance = ec2.create_instances(
#     MinCount = 1,
#     MaxCount = 1,
#     ImageId = "ami-0c02fb55956c7d316",
#     InstanceType='t2.micro',
#     KeyName = 'dev',
#     # SecurityGroupIds=[
#     #     security_group.id
#     # ],
#     IamInstanceProfile={
#         'Name': 'ec2role'
#     },
#     TagSpecifications=[
#         {
#             'ResourceType': 'instance',
#             'Tags': [
#                 {
#                     "Key": "Name",
#                     "Value": "ec2-instance"
#                 },
#             ]
#         },
#     ],
#     BlockDeviceMappings=[
#         {
#             'DeviceName': '/dev/sdh',
#             'VirtualName': 'volume',
#             'Ebs': {
#                 'VolumeSize': 15,
#                 'VolumeType': 'gp2',
#                 # 'KmsKeyId': 'aws/ebs',
#                 'Encrypted': True
#             },
#         },
#     ]
# )
# for instance in instance:
#     print(f'ec2"{instance.id}" has been launched')
# print(instance.id)






# instance.wait_until_running()
# print(f'ec2"{instance.id}" has been started')
  
# ebs = ec2.create_volume(
#     Size = 10,
#     Encrypted= True,
#     AvailabilityZone = 'us-east-1c',
#     TagSpecifications=[
#         {
#             'ResourceType': 'volume',
#             'Tags': [
#                 {
#                     "Key": "Name",
#                     "Value": "ec2-ebs"
#                 },
#             ]
#         },
#     ]
# )
# ebs.create_tags(
#     Tags=[{"Key":"Name","Value":"ebs-dev"}])

# volume = ec2.Volume(ebs.id)
# ebs.attach_to_instance(
#     VolumeId = ebs.id,
#     Device = '/dev/sdh',
#     InstanceId = instance.id,
#     )
# print(f'Created volume ID: {ebs.id}')
# print(f'Volume {ebs.id} status -> {ebs.state}')
