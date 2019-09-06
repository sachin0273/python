"""

Purpose:in this program we prints roots of given equation input
author : sachin shrikant jadhav
version:3.7
since  : 22-08-2019

"""

from Utility.utility import Qudratic


def Qudratic_Driver():
    while True:
        try:
            A = int(input("enter value of A "))
            B = int(input("enter value of B "))
            C = int(input("enter value of C "))
            if 0 < A and B and C < 101:
                result = Qudratic(A, B, C)  # here we calling function from utility
                print(result)
                break
            else:
                print("please enter valid input value between 1 to 100")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Qudratic_Driver()
