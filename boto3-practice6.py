import boto3
import glob 

s3_resource = boto3.client('s3')
files = glob.glob("/tmp/*.png")
#upload multiple .png files from /tmp/ dir to s3 bucket
for file in files:
    s3_resource.upload_file(
        Filename=file,
        Bucket="omarboto3bucketpractice2",
        Key=file.split("/")[-1])