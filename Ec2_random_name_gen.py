#!/usr/bin/env python3

import string, random

#Initial list of departments
departments = ('Marketing', 'Accounting', 'FinOps')

#Input number of instances and dpeartment name
number_of_instances = int(input("Please enter the number of EC2 instnaces: "))
department = str(input("Please enter a department name: "))
#function to search item
def getDepartment():
   for i in departments:
       if department.casefold()==i.casefold():
           return True
 
   else:
       return False
 
if getDepartment():
   
  # If function returns true
   print('The department that you have entered is present')
 
else:
   
  # If function returns false
   print('Classroom you are searching is not present')