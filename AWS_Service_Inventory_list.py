# AWS Service inventory - Create a list of AWS services using Python

# Create intial empty list
aws_services = []

# Populate the list with AWS services
for service in ["S3", "VPC", "RDS", "DynamoDB", "EC2", "CloudWatch"]:
    aws_services.append(service)
    
# Print the list & list length
print(aws_services)
print(len(aws_services))

# Remove S3 & DynamoDB services from the list
aws_services.remove("S3")
aws_services.remove("DynamoDB")

# Print the list & list length
print(aws_services)
print(len(aws_services))