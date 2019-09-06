"""

Purpose:in this program we read the integer word file as unsorted and prints the in sorted format
author : sachin shrikant jadhav
version:3.7
since  : 24-08-2019

"""

from Utility.utility import Bubble_Sort
from Utility.utility import File_Int_Reader


def Bubble_Sort_Driver():
    try:
        word = File_Int_Reader("integer.txt")  # here we calling integer file reader function from Utility
        result = Bubble_Sort(word)  # here we calling bubble sort function from utility
        print(result)
    except FileNotFoundError:
        print("please enter valid file path")


if __name__ == '__main__':
    Bubble_Sort_Driver()
