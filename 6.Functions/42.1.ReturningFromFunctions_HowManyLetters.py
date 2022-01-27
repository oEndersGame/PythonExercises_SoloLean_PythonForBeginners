# Problem:
'''
Write a function that takes a string and a letter as its arguments and returns the count of the letter in the string.

Sample Input:
hello, how are you?
o
Sample Output:
3

Explanation: The letter o appears 3 times in the given text.

NOTE: The given code takes the string and letter from input and passes them to the letter_count() function.
Define the function, so that the given code works as expected.
'''
# -----------------------------------------#

# CODE:

#function_with_input-parmeters:
def letter_count(text, letter):
    #for_loop:
    count = 0
    for i in text:
        if i == letter:
            count = count + 1
    return count

#input_text&letter:
text = input()
letter = input()
#output_solution:
print(letter_count(text, letter))