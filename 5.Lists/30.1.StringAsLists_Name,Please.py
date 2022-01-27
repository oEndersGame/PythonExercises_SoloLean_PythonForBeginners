# Problem:
'''
You need to take the first and last name of a person as input and output
the initials (first letters of the first and last name).

Sample Input:
James
Smith
Sample Output:
J.S.

NOTE: In order to match the output, you need to place dots after each initial.
'''
# -----------------------------------------#

# CODE:

fname = input()
lname = input()
#your code goes here
print(fname [0]+"."+lname[0]+".")