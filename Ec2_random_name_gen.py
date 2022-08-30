#!/usr/bin/env python3

import string, random
from itertools import repeat

#Departments 
#departments = ('Marketing', 'Accounting', 'FinOps')

#Input number of instances and dpeartment name
number_of_instances = int(input("Please enter the number of EC2 instnaces required: "))
department = str(input("Please enter a department name: "))

#function
def getName():
    output = ''
    for _ in repeat(None, number_of_instances):
            extra = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
            output = department + extra
            return output
for i in repeat(None, number_of_instances):
    print(getName())