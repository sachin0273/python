"""

Purpose:in this program we prints given year is leap or not
author : Sachin Shrikant Jadhav
version:3.7
since  : 21-08-2019

"""

from Utility.utility import Leap_Or_Not
while True:
    try:
        year = int(input("please enter year"))
        leap_year = len(str(year))
        if leap_year == 4:
            result = Leap_Or_Not(year)  # here we calling function from utility
            break
        else:
            print("please enter 4 digit year")
    except ValueError:
        print("please enter valid input")
