import boto3
resource = boto3.resource("s3")
if len(list(resource.buckets.all())) > 0:
    print("The following " + str(len(list(resource.buckets.all()))) + " S3 bucket(s) exist(s) in your AWS account:")
else:
    print("You have " + str(len(list(resource.buckets.all()))) + " S3 buckets in your AWS account")
for bucket in resource.buckets.all():
    print(bucket.name)
