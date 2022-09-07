import boto3
#Describe instances. Filter for running instances in the dev Environment
client = boto3.client('ec2')
response = client.describe_instances(
    Filters=[{
        'Name': 'instance-state-name', 'Values': ['running']
        },           
        {
                'Name': 'tag:Environment', 'Values': ['dev']
        }
    ])
print(response)