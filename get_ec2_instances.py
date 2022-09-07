import boto3


#Describe instances. Filter for running instances in the dev Environment
client = boto3.client('ec2')
running_dev_clients = client.describe_instances(
    Filters=[{
        'Name': 'instance-state-name', 'Values': ['running']
        },           
        {
                'Name': 'tag:Environment', 'Values': ['dev']
        }
    ])

#loop to get instance IDs for the running dev instances
dev_ids = []
for reservation in running_dev_clients['Reservations']:
    for instance in reservation['Instances']:
        dev_id = instance['InstanceId']
        dev_ids.append(dev_id)
    print(dev_ids)


#Stop any running dev instnaces
for i_d in dev_ids:
    response = client.stop_instances(
    InstanceIds=[
        i_d,
    ],
)