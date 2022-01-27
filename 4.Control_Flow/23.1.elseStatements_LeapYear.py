# Problem:
'''
You need to make a program to take a year as input and
output "Leap year" if it’s a leap year, and "Not a leap year", if it’s not.
To check whether a year is a leap year or not, you need to check the following:
1) If the year is evenly divisible by 4, go to step 2. Otherwise, the year is NOT leap year.
2) If the year is evenly divisible by 100, go to step 3. Otherwise, the year is a leap year.
3) If the year is evenly divisible by 400, the year is a leap year. Otherwise, it is not a leap year.

Sample Input:  2000
Sample Output: Leap year

Use the modulo operator % to check if the year is evenly divisible by a number.

NOTE: A year is called a leap year if it contains an additional day which
makes the number of the days in that year is 366.
This additional day is added in February which makes it 29 days long.
'''
# -----------------------------------------#

# CODE:

year = int(input())
#your code goes here
def check_year(x):
    if x%400 == 0:
        print("Leap year")
    elif x%100 == 0:
        print("Not a leap year")
    elif x%4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
    return

check_year(year)