"""

Purpose:in this program we prints the harmonic number of given nth number
author : Sachin Shrikant Jadhav
version:3.7
since  : 21-08-2019

"""

from Utility.utility import Harmonic_Number


def Harmonic_Driver():
    while True:
        try:
            Nth_number = int(input("please enter your number"))
            if 0 < Nth_number < 101:
                result = Harmonic_Number(Nth_number)  # here we calling harmonic number function from utility
                print(result)
                break
            else:
                print("please enter number between 1 to 100")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Harmonic_Driver()
