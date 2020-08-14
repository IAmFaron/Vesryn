# -*- coding: utf-8 -*-
### Generate a random date in Month/DD format, along with its season, for a standard Rekula Calendar year.
import random

def int2ordinal(i):
    #Convert the integer to a string
    s_int = str(i)
    #initialize second_last for single-digit numbers
    second_last = 0
    #Identify the last and second last digits and decide a suffix   
    last = s_int[len(s_int) - 1]
    second_last = s_int[len(s_int) - 2]
    if last == "1" and second_last != "1":
        suffix = "st"
    elif last == "2" and second_last != "1":
        suffix = "nd"
    elif last == "3" and second_last != "1":
        suffix = "rd"
    else:
        suffix = "th"
    ordinal = s_int + suffix
    return(ordinal)

def randomDate():

# Define an ordered list of months
    months = ["Evendon","Haledon","Urodon","Relgadon","Gryphos","Aurumos","Carthanos","Taranos","Fenral","Dinral","Aeruval","Xephral","Laliana","Gilgala","Florana","Alamyst"]
# Choose a month
    month = random.choice(months)
# Get the month's number
    for i in range(16):
        if months[i] == month:
            num_month = 1 + i
# Match the month with its season
    if month[-1] == 'n':
        season = 'spring'
    elif month[-1] == 's':
        season = 'summer'
    elif month[-1] == 'l':
        season = 'autumn'
    else:
        season = 'winter'
        
# Generate a random day from 1-28
    day = randint(1, 28)
    day_ord = int2ordinal(day)
# Return a formatted message
    print("Your date is the ", day_ord, " of ", month, " (", day, "/", num_month, ")\nThis is a ", season, " month.",sep="")
    
def main():
# Initialize loop
    again = 'y'
    while again == 'y':
        # Get first date
        randomDate()
         # Check for continuation
        again = str(input("Generate another date? (y/n): "))


main()

