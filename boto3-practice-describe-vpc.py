import boto3

client=boto3.client('ec2')
response = client.describe_vpcs()
response
print(response)