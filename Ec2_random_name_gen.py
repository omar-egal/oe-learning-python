#!/usr/bin/env python3

import string, random
from itertools import repeat

#Departments 
departments =  ['Marketing', 'Accounting', 'FinOps']

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
            

#Loop to repeat fuction for the number of instances entered
c = departments.count(department.title())
if c > 0:
    print("The EC2 name generator cannot be used with the department: " + department + ". Please enter the name of a different department")
else:
    for i in repeat(None, number_of_instances):
        print(getName())
    