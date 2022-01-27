# Problem:
'''
You’re working on a search engine. Watch your back Google!
The given code takes a text and a word as input and passes them to a function called search().
The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

Sample Input:
"This is awesome"
"awesome"
Sample Output:
Word found

NOTE: Define the search() function, so that the given code works as expected.
'''
# -----------------------------------------#

# CODE:

#input_text&letter:
text = input()
word = input()
#search-function:
def search(text, word):
    if word in text.split():
        print("Word found")
    else:
        print("Word not found")
#calling_search-function:
search(text, word)