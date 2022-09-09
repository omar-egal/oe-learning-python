import boto3
import json

client=boto3.client('ec2')
response = client.delete_vpc(
    VpcId='vpc-001d9b5835e1dcb7c',
    )
print(json.dumps(response, indent=2, default=str))

