from datetime import datetime
import boto3

ec2_client = boto3.client('ec2')

def lambda_handler(event, context):
    # Get list of regions
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    for region in regions:
        print('Instances in EC2 Region {0}:'.format(region))
        ec2 = boto3.resource('ec2', region_name=region)
        
        # Get only instnaces whre the backup tag has a value of true
        instances = ec2.instances.filter(
            Filters=[
                {'Name': 'tag:backup', 'Values': ['true']}
            ]
        )
            
        # ISO 8601 timestamp, i.e. 2019-01-31T14:01:58
        timestamp = datetime.now().replace(microsecond=0).isoformat()
        
        for i in instances.all():
            for v in i.volumes.all():
                desc = 'Backup of {0}, volume {1}, created {2}'.format(i.id, v.id, timestamp)
            print(desc)
            
            snapshot = v.create_snapshot(Description=desc)
            
            print('Created snapshot:', snapshot.id)