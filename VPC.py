# vpc = ec2.create_vpc(
#     CidrBlock='10.0.0.0/16')

# vpc.create_tags(
#     Tags=[{"Key":"Name","Value":"my_vpc"}])

# vpc.wait_until_available()
# print(vpc.id)

# # response = vpc.delete()

# subnet = ec2.create_subnet(
#     CidrBlock = '10.0.2.0/24',
#     VpcId= vpc.id,
#     AvailabilityZone = 'us-east-1a',
# )
# subnet.create_tags(
#     Tags=[{"Key":"Name","Value":"btot3-sub"}])
# print(subnet.id)


# security_group = ec2.create_security_group(
#     Description='Allow inbound SSH traffic',
#     GroupName='security_group',
#     # VpcId=vpc.id,
#     TagSpecifications=[
#         {
#             'ResourceType': 'security-group',
#             'Tags': [
#                 {
#                     'Key': 'Name',
#                     'Value': 'allow-inbound-ssh'
#                 },
#             ]
#         },
#     ],
# )
# security_group.authorize_ingress(
#     CidrIp='0.0.0.0/0',
#     FromPort=22,
#     ToPort=22,
#     IpProtocol='tcp',   
# )
# print(f'Security Group {security_group.id} has been created')

# security_group.delete()
# print(f'Security Group {security_group.id} has been deleted')
