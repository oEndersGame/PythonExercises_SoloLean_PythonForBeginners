# Problem:
'''
Did you know that there are more bacteria cells in your body than cells that make up your body? Weird!
A bacteria culture starts with 500 bacteria and doubles in size every hour.
Which means, after 1 hour the number of bacteria is 1000, after 2 hours - 2000, and so on.
Let’s calculate and output the number of bacteria that will be in the culture after 24 hours.

NOTE: The formula to calculate the bacteria after N hours will be: 500*2ᴺ
'''
# -----------------------------------------#

# CODE:

def bac_calc():
    hours = 24
    bacteria_num = 500 * 2 ** hours
    return bacteria_num


print(bac_calc())