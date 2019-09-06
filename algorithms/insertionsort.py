"""
Purpose:in this program we read the word file as unsorted and prints the in sorted format
author : sachin shrikant jadhav
version:3.7
since  : 24-08-2019

"""
from Utility.utility import Insertion_Sort
from Utility.utility import File_Reader


def Insertion_Sort_Driver():
    try:
        word = File_Reader("new.txt")  # here we calling file reader function from Utility
        word_list = word.split(",")
        result = Insertion_Sort(word_list)  # here we calling insertion function from Utility
        print(result)
    except FileNotFoundError:
        print("please enter valid file path")


if __name__ == '__main__':
    Insertion_Sort_Driver()
