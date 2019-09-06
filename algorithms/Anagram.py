"""

Purpose:in this program we prints given both strings are anagram or not for each other
author : sachin shrikant jadhav
version:3.7
since  : 23-08-2019

"""
from Utility.utility import Is_Anagram


def Anagram_Driver():
    while True:
        try:
            first_string = input("please enter your first name")
            second_string = input("please enter your second name")
            if first_string.isalpha()and second_string.isalpha():
                result = Is_Anagram(first_string, second_string)  # here we calling function from utility
                if result:
                    print("is anagram")
                else:
                    print("is not anagram")
                break
            else:
                print("please enter valid input in char")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Anagram_Driver()
