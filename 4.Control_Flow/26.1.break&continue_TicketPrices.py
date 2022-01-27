# Problem:
'''
You are making a ticketing system.
The price of a single ticket is $100.
For children under 3 years old, the ticket is free.
Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.
Sample Input:
18
24
2
5
42
Sample Output:
400

NOTE: There is one child under 3 among the passengers, so the total price of 5 tickets will be $400.
'''
# -----------------------------------------#

# CODE:

def tic_calc():
    tic_price = 0
    i = 1
    while i <= 5:
        x = int(input())
        # your code goes here
        if x >= 4:
            tic_price += 100
            i += 1
        else:
            i += 1
            continue
    print(tic_price)

tic_calc()