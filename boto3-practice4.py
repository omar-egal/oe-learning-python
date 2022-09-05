import boto3
s3_resource = boto3.client('s3')
#list all bucket names and their creation dates
for bucket in s3_resource.list_buckets()["Buckets"]:
    print("S3 Bucket:",bucket['Name']," Creation date:", bucket['CreationDate'])