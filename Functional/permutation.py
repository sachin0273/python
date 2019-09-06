"""

Purpose:in this program we prints the all permutation of given string
author : sachin shrikant jadhav
version:3.7
since  : 22-08-2019

"""
from Utility.utility import Permutation


def Permutation_Driver():
    while True:
        try:
            string = input("enter a string")
            if 0 < len(string) < 10:
                if string.isalpha():
                    result = Permutation(string)  # here we calling function from utility
                    print(len(result))
                    print(result)
                    break
                else:
                    print("please enter valid string in character")
            else:
                print("please enter valid string length should be 1 to 9")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Permutation_Driver()
