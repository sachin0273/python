"""

Purpose:in this program we prints the triplets given list as addition of the triplets is equal to zero
author : sachin shrikant jadhav
version:3.7
since  : 22-08-2019

"""
from Utility.utility import Triplets


def Triplets_Driver():
    try:
        array = [-1, -3, 9, -2, 8, 9, 4]
        length_array = len(array)
        result = Triplets(array, length_array)  # here we calling function from utility
        print(result)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    Triplets_Driver()
