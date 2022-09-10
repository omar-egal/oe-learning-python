import boto3
import json

#Find the instance IDs of EC2 instances
ec2_client = boto3.client('ec2')
instances = ec2_client.describe_instances()
data = instances['Reservations'][0]
data_instance = data['Instances']
for i in range(len(data_instance)):
    print(f'The Instnace ID is: {data_instance[i]["InstanceId"]}')