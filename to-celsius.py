#!/usr/bin/env python3.7

# Python implementation goes here

farenheit = float(input("What temperature (in Farenheit) would you like converted to Celsius? "))
celsius = (farenheit -32) * 5 / 9

print(farenheit, "F is", round(celsius, 2), "C")