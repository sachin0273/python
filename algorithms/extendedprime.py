"""

Purpose:in this program we check the prime number given range and print the palindrome and anagram primenumber
author : sachin shrikant jadhav
version:3.7
since  : 23-08-2019

"""
from Utility.utility import Prime_Number


def Reverse(number):  # here is the function for the reverse number
    try:
        reverse_number = 0
        while number > 0:
            lastDigit = number % 10
            reverse_number = (reverse_number * 10) + lastDigit
            number = number // 10
        return reverse_number
    except ValueError as e:
        print(e)


def Prime_Palindrome(prime_num):  # here is function for prime number is palindrome or not
    try:
        prime_palindrome_list = []
        for prime_number in prime_num:
            for prime in prime_num:
                if prime > 7:
                    palindrome = Reverse(prime)  # here we call the number reverse function
                    if prime_number == palindrome:
                        prime_palindrome_list.append(prime_number)
                        print(prime_number, "-->", prime, "this are palindrome and anagrams for each other")
        return prime_palindrome_list
    except Exception as e:
        print(e)


def Palindrome_or_Anagram_Driver():  # here is the driver function of program
    try:
        prime_num = Prime_Number(1000)
        result = Prime_Palindrome(prime_num)
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    Palindrome_or_Anagram_Driver()
