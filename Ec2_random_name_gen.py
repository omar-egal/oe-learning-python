#!/usr/bin/env python3

import string, random

#Departments 
#departments = ('Marketing', 'Accounting', 'FinOps')

#Input number of instances and dpeartment name


#function
def getName():
    output = ''
    number_of_instances = int(input("Please enter the number of EC2 instnaces required: "))
    department = str(input("Please enter a department name: "))
    while number_of_instances > 0:
        extra = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
        output = department + extra
        number_of_instances -= 1
    return output
print(getName())