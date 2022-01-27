# Problem:
'''
Now that we know how to combine multiple conditions, let’s improve our
gold purity checker program and output the corresponding purity level in Karats!
Here is the purity chart we’ll be using:
24K – 99.9%
22K – 91.7%
20K – 83.3%
18K – 75.0%
If the percentage is between 75 and 83.3, the gold is considered to be 18K.
If it's between 83.3 and 91.7 - then it’s 20K, and so on.
Given the percentage as input, output the corresponding Karat value, including the letter K.

Sample Input:  92.4
Sample Output: 22K

NOTE: Do not output anything, if the percentage is lower than 75%.
'''
# -----------------------------------------#

# CODE:

purity = float(input())
#your code goes here
def purity_level(x):
    if x >= 99.9:
        print("24K")
    elif x >= 91.7 and x <99.9:
        print("22K")
    elif x >= 83.3 and x < 91.7:
        print("20K")
    elif x >= 75 and x < 83.3:
        print("18K")
    else:
        pass

purity_level(purity)
