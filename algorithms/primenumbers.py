"""

Purpose:in this program we prints prime number in user input range
author : sachin shrikant jadhav
version:3.7
since  : 23-08-2019

"""
from Utility.utility import Prime_Number


def Prime_Driver():
    while True:
        try:
            prime_range = int(input("enter a range"))
            if 0 < prime_range < 1001:
                result = Prime_Number(prime_range)  # here we calling function from utility
                print(result)
                break
            else:
                print("please enter valid number between 1 to 1000")

        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Prime_Driver()
