#How to create a VPC using boto3
import boto3

client = boto3.client('ec2')
response = client.create_vpc(
    CidrBlock='10.0.2.0/16',
    AmazonProvidedIpv6CidrBlock=False,
    InstanceTenancy='default',
    TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto3-vpc'
                },
            ]
        },
    ]
)
