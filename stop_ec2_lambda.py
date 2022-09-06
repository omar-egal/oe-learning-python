#!/usr/bin/env python3


import boto3



running_instances = []
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if instance['State']['Name'] == 'running':
           x = (instance['Tags'][0])
           y = (instance['Tags'][1])
           #print(x)
           running_instances.append(x)
           running_instances.append(y)
print(running_instances)


#ec2 = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
#instance_id = ec2.text
#print(instance_id)

