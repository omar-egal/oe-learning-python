import boto3
s3_resource = boto3.client('s3')
for bucket in s3_resource.list_buckets()["Buckets"]:
    print("S3 Bucket:",bucket['Name']," Creation date:", bucket['CreationDate'])
 #   print(bucket['CreationDate'])