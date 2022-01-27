# Problem:
'''
Random task! You need to calculate the number of hours in 888 minutes.
Your program needs to output the number of hours and then the number of remaining minutes, on separate lines.
For example, 72 minutes are equal to 1 hour and 12 minutes, so your program would output:
1
12

NOTE: You can use floor division to find the number of hours, and the modulo operator to find the remaining minutes.
Use separate print() statements for each output.
'''
# -----------------------------------------#

# CODE:
min = 888

def num_of_hours():
    result = min // 60
    return result

def remain_mins():
    result = min % 60
    return result

print( num_of_hours() )
print( remain_mins() )