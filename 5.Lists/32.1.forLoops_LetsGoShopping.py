# Problem:
'''
You’re making a shopping cart program.
The shopping cart is declared as a list of prices, and you need to add functionality to apply a discount and output the total price.
Take the discount percentage as input, calculate and output the total price for the shopping cart.

NOTE: Use a for loop to iterate over the list.
Use the following formula to calculate the result of X% discount on $Y price: Y - (Y*X/100)
'''
# -----------------------------------------#

# CODE:

cart = [15, 42, 120, 9, 5, 380]

def dis_calculator():
    discount = int(input())
    total = 0

    for i in cart:
        total = total + i * discount / 100
        disc_price = sum(cart) - total
    print(disc_price)

dis_calculator()