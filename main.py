import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

vpc = ec2.create_vpc(
    CidrBlock='10.0.0.0/16')

vpc.create_tags(
    Tags=[{"Key":"Name","Value":"my_vpc"}])

vpc.wait_until_available()
print(vpc.id)

subnet = ec2.create_subnet(
    CidrBlock = '10.0.2.0/24',
    VpcId= vpc.id,
    AvailabilityZone = 'us-east-1a',
)
subnet.create_tags(
    Tags=[{"Key":"Name","Value":"btot3-sub"}])
print(subnet.id)


security_group = ec2.create_security_group(
    Description='Allow inbound SSH traffic',
    GroupName='security_group',
    VpcId=vpc.id,
    TagSpecifications=[
        {
            'ResourceType': 'security-group',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'allow-inbound-ssh'
                },
            ]
        },
    ],
)
security_group.authorize_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=22,
    ToPort=22,
    IpProtocol='tcp',   
)
print(f'Security Group {security_group.id} has been created')

# security_group.delete()
# print(f'Security Group {security_group.id} has been deleted')

instance = ec2.Instance('id')
instance = ec2.create_instances(
    MinCount = 1,
    MaxCount = 1,
    ImageId = "ami-0c02fb55956c7d316",
    InstanceType='t2.micro',
    SubnetId = subnet,
    KeyName = 'dev',
    SecurityGroupIds=[
        security_group.id
    ],
    IamInstanceProfile={
        'Name': 'ec2role'
    },
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    "Key": "Name",
                    "Value": "ec2-instance"
                },
            ]
        },
    ]
)
for instance in instance:
    print(f'ec2"{instance.id}" has been launched')
print(instance.id)
# instance.wait_until_running()
# print(f'ec2"{instance.id}" has been started')
  
