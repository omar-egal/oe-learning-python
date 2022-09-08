import json
import boto3
import botocore

region = 'us-east-1'
client = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    
    #Describe instances --> Filter for running instnaces --> Filter for env, dev tags 
    running_dev_clients = client.describe_instances(
    Filters=[{
        'Name': 'instance-state-name', 'Values': ['running']
        },           
        {
                'Name': 'tag:Environment', 'Values': ['dev']
        }
    ]
    )
    
    #Loop to get instance IDs for the running dev instances
    dev_ids = []
    for reservation in running_dev_clients['Reservations']:
        for instance in reservation['Instances']:
            dev_id = instance['InstanceId']
            dev_ids.append(dev_id)

    #Stop any running dev instnaces according to the instance IDs
    if len(dev_ids) != 0:
        try:
            print("Stopping running instances in the dev environment...")
            for i_d in dev_ids:
                client.stop_instances(
                InstanceIds=[
                    i_d,
                ],
            )
        except botocore.exceptions.ClientError as error:
            print("There are currently no running instnaces with the tag: Environment --> dev" + error)

        response = "Successfully stopped running instances in the dev environment: " + str(i_d)
        print(response)
    
    return {
        'statusCode': 200
    }