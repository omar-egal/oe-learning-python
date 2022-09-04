import boto3
aws_resource = boto3.resource("s3")
bucket = aws_resource.Bucket("omarboto3bucketpractice2")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1'
    },

)

print(response)