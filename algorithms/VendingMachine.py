"""

Purpose:in this program  There is 1,2,5,10,50,100,500 and 1000 Rs Notes which can be
        returned by Vending Machine. so we  calculate the minimum number of Notes as
        well as the Notes to be returned by the Vending Machine as a change
author : sachin shrikant jadhav
version:3.7
since  : 24-08-2019

"""

from Utility.utility import Vending


def Vending_Driver():
    while True:
        try:
            amount_to_change = int(input("enter your amount to change"))
            if 0 < amount_to_change < 100001:
                result = Vending(amount_to_change)  # here we calling vending function from UtilityS
                print("minimum number of notes required is====", result)
                break
            else:
                print("please enter valid value between 1 to 100000")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Vending_Driver()
