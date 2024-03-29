"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we create the unordered linked list for word word read from text file
author:  Sachin Shrikant Jadhav
since :  26-08-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""

from Utility.utility import File_Reader
from Utility.utility import File_Writer
from data_structure.my_linked_list import Linked_List

""" here we create the object"""
linked = Linked_List()


def Unorderd_Linked_List_Driver():
    """

    :purpose: in this function we get input from user like search element and word from file
    :return: this return unordered linked list of word from txt file

    """
    try:
        result = File_Reader("data.txt")  # here we calling file_reader function from utility class
        word_list = result.split(",")

        for i in word_list:
            linked.Add_To_End(i)  # here we adding word in linked list by calling add function from linked_list class
        linked.Display()
        print()
        while True:
            word_for_search = input("enter your word for search  = ")
            if word_for_search.isalpha() and len(word_for_search) < 9:
                linked.Search_Element_Add_Or_Delete(word_for_search)  # here we calling search function from linked_list
                # class
                result = linked.Display_Return()
                File_Writer("write_data.txt", result)  # file writer function
                linked.Display()
                break
            else:
                print("please enter valid word in char or length should be less than 9")
    except FileNotFoundError:
        print("please enter valid file path")


if __name__ == '__main__':
    unorderd_linked_list_Driver()
