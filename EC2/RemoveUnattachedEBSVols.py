import boto3
ec2_client = boto3.client('ec2')

def lambda_handler(object, context):
    
    # Get list of regions
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    # Iterate over each region
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        print("Region:", region)
        
        
    # List only unattavhed volumes ('available' vs 'in-use')
    volumes = ec2.volumes.filter(
        Filters=[{'Name': 'status', 'Values': ['available']}])
        
    for volume in volumes:
        v = ec2.Volume(volume.id)
        print("Deleting EBS volume: {}, Size: {} GiB".format(v.id, v.size))