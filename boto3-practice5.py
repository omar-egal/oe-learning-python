import boto3 
s3_resource = boto3.client('s3')

#upload single file from /tmp/ dir to s3 bucket
s3_resource.upload_file(
    Filename="/tmp/uploadtest.png",
    Bucket="omarboto3bucketpractice2",
    Key="uploadtest_uploaded.png")