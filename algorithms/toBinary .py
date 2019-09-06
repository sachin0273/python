"""

Purpose:in this program we take number from user and prints the binary of that number
author : sachin shrikant jadhav
version:3.7
since  : 24-08-2019

"""

from Utility.utility import To_Binary


def Binary_Driver():
    while True:
        try:
            number = int(input("please enter a number"))
            if 0 < number < 101:
                result = To_Binary(number)  # here we calling to_binary function from utility
                print(result)
                break
            else:
                print("please enter valid number between 1 to 100")
        except ValueError:
            print("please enter  valid input")


if __name__ == '__main__':
    Binary_Driver()
