# Problem:
'''
You need to make a function that converts a foot value to inches.
1 foot has 12 inches.
Define a convert() function, that takes the foot value as argument and outputs the inches value.

NOTE: The given code takes the foot value as input and passes it to the convert function. Define the convert function, so that the given code works.
'''
# -----------------------------------------#

# CODE:
feet = int(input())

def convert(feet):
    inch = feet * 12
    print(inch)

convert(feet)