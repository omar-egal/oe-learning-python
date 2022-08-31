#!/usr/bin/env python3

#Several departments share an AWS environment. 
#You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. 
#Use Python to create your unique EC2 names that the users can then attach to the instances.
#1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
#2. Allow the user to input the name of their department that is used in the unique name.
#3. Generate random characters and numbers that will be included in the unique name.
#The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments. 
#List these departments as options and if a user puts another department, print a message that they should not use this Name Generator. 
#Be sure to account for incorrect upper or lowercase letters in the correct department. 
#Example: a user inputs accounting vs Accounting.

import string, random
from itertools import repeat

#Departments 
departments =  ['Marketing', 'Accounting', 'FinOps']
departments_lower = map(str.lower, departments)

#Number of instances and department name
number_of_instances = int(input("Please enter the number of EC2 instnaces required: "))
department = str(input("Please enter a department name: "))

#function to add random numbers and characters to department name as EC2 instance name
def getName():
    output = ''
    for _ in repeat(None, number_of_instances):
            extra = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
            output = department + '_' + extra
            return output
            

#Check if entered department is viable to use with generator
if department.lower() in departments_lower:
    print("The EC2 name generator cannot be used with the department: " + department + 
    ". Please enter the name of a different department")
else:
    #Repeat output based on number of instances
    for i in repeat(None, number_of_instances):
        print(getName())