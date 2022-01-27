# Problem:
'''
You are making a game! The player tries to shoot an object and can hit or miss it.
The player starts with 100 points, with a hit adding 10 points to the player’s score, and a miss deducting 20 points.
Your program needs to take 4 action results as input ("hit" or "miss"), calculate and output the player’s remaining points.

Sample Input:
hit
hit
miss
hit
Sample Output:
110

Explanation: 3 hits add 30 points, one miss deducts 20, making the total points equal to 110.

NOTE: Use a while loop to take input during each iteration and calculate the points.
'''
# -----------------------------------------#

# CODE:
###shoot-function:
def shoot():
    lifepoints = 100
    round = 1
####while-loop:
    while round <= 4:
        action = input()
        round += 1
########if/else-statemen:
        if action == "hit":
            lifepoints += 10
        else:
            lifepoints -= 20
####print-solution:
    print(lifepoints)
#executing-shoot-function:
shoot()
