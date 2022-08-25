# AWS Service inventory - Create a list of AWS services using Python

# Create intial empty list
aws_services = []

# Populate the list with AWS services
for service in ["S3", "VPC", "RDS", "DynamoDB", "EC2", "CloudWatch"]:
    aws_services.append(service)
    
# Print the list & list length
print(aws_services)
print("These are currently " + str(len(aws_services)) + " services in the service inventory.")

# Remove remove two services from the list
aws_services.pop() #removes the last element in the list
aws_services.pop(2) #removes the 3rd element in the list

# Print the list & list length
print(aws_services)
print("There are currently " + str(len(aws_services)) + " services remaining in the inventory.")