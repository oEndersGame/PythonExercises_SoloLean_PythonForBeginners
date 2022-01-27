# Problem:
'''
The seats in your ticketing program are stored in a 2D list. Each seat is assigned a letter code.
Complete the program to take the seat row and column as input and output the corresponding code
from the list (row and column indices start from 0).

Sample Input:
3
2
Sample Output:
l

NOTE: Note, that you need to convert the input() to int, in order to use it as an index.
'''
# -----------------------------------------#

# CODE:

seats = [
['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', 'i'],
['j', 'k', 'l']
]
#your code goes here
row     = int(input())
column  = int(input())
print(seats[row][column])