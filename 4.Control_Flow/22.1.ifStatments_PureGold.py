# Problem:
'''
You’re making a gold purity checker, that should accept only 22K or 24K gold. Only the good stuff!
22K gold has 91.7% or more gold in it, while 24K corresponds to 99.9% and above purity.
Given the % of gold purity as input, you should output "Accepted" only if it corresponds to 22 or 24K.
Sample Input:   93.4
Sample Output:  Accepted

NOTE:  Do not output anything if the gold corresponds to lower purity levels.
'''
# -----------------------------------------#

# CODE:

purity = float(input())

#funktionslösung
def quality_check(x):
    if x >= 91.7 and x <= 100:
        print ("Accepted")
    else:
        pass

quality_check(purity)