import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

instance = ec2.Instance('i-0bfebbdb5a7f41378')
instance.terminate()
instance.wait_until_terminated()
print(f'instance has been terminated')

security_group = ec2.SecurityGroup('sg-05ada57202e2cf996')
security_group.delete()
print(f'security Group has been deleted')

subnet = ec2.Subnet('subnet-09d3981accfe7a15b')
subnet.delete()
print(f'subnet has been deleted')

vpc = ec2.Vpc('vpc-0f7a53ab758ddc8c9')
vpc.delete()
print(f'vpc has been deleted')
