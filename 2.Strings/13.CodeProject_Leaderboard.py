# Problem:
'''
You need to make a program for a leaderboard.
The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot:
1.
2.
3.
...

NOTE: You can use the \n newline character to create line breaks,
or, alternatively, create the desired output using three double quotes """.
'''
# -----------------------------------------#

# CODE:


# your code goes here
def printer():
    v = ""
    for i in range(1, 10):
        v = v + (str(i) + "." + "\n")
    return v

print(printer())