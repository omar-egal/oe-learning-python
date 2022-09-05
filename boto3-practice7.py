import boto3

#List objects in the bucket
s3_resource = boto3.client('s3')
objects = s3_resource.list_objects(Bucket="omarboto3bucketpractice2")["Contents"]
for i in objects:
    print(i["Key"])