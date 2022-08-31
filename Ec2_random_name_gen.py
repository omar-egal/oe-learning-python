#!/usr/bin/env python3

import string, random
from itertools import repeat

#Departments 
departments =  ['Marketing', 'Accounting', 'FinOps']
departments_lower = map(str.lower, departments)

#INumber of instances and dpeartment name
number_of_instances = int(input("Please enter the number of EC2 instnaces required: "))
department = str(input("Please enter a department name: "))

#function to add random numbers and characters to department name as EC2 instance name
def getName():
    output = ''
    for _ in repeat(None, number_of_instances):
            extra = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
            output = department + '_' + extra
            return output
            

#Check if entered department us viable to use with generator
if department.lower() in departments_lower:
    print("The EC2 name generator cannot be used with the department: " + department + 
    ". Please enter the name of a different department")
else:
    #Repeat output based on number of instances
    for i in repeat(None, number_of_instances):
        print(getName())
    