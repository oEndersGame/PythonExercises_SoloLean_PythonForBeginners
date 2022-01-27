# Problem:
'''
You’re making a voice recognition system.
The supported commands are stored in a list.
Complete the program to take a command as input, check if it’s supported
and output "OK", if it is, and "Not supported", if not.

Sample Input:
Lights Off
Sample Output:
OK

NOTE: The given code declares the list of supported commands.
'''
# -----------------------------------------#

# CODE:

commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]

#your code goes here
voice = input()

if voice in commands:
    print("OK")
else:
    print("Not supported")