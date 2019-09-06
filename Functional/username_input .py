"""

 Purpose:in this program we prints the string with input username
 author : Sachin Shrikant Jadhav
 version:3.7
 since  : 21-08-2019

"""

from Utility.utility import User_Name

while True:
    your_user_name = input("please enter your name")
    length = len(your_user_name)
    if your_user_name.isalpha() and length < 4:
        result = User_Name(your_user_name)  # calling user_name function from utility
        print(result)
        break
    else:
        print("please enter valid input")
