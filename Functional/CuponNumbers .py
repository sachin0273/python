"""

Purpose:in this program we prints the distinct number of coupns as user input
author : Sachin Shrikant Jadhav
version:3.7
since  : 22-08-2019

"""
from Utility.utility import Coupn


def Distinct_Coupn_Driver():
    while True:
        try:
            number_of_coupons = int(input("please number of coupons you want"))
            if 0 < number_of_coupons < 500:
                coupons = Coupn(number_of_coupons)  # here we calling function from utility
                print(coupons)
                break
            else:
                print("please enter number between 1 to 500")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Distinct_Coupn_Driver()
