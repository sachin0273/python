"""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we create the ordered linked list for word,word read from text file
author:  Sachin Shrikant Jadhav
since :  26-08-2019
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""

from Utility.utility import File_Int_Reader, File_Writer
from data_structure.my_linked_list import Linked_List
from Utility.utility import Bubble_Sort

""" here we creating object"""

linked = Linked_List()


def Ordered_Linked_List_Driver():
    """

    :return: this function is used for creating ordered linked list for integer data ,integer data read from file

    """
    try:
        integer_result = File_Int_Reader("integer_data.txt")
        sorted_numbers = Bubble_Sort(integer_result)  # here sort function calling from utility class
        for number in sorted_numbers:
            linked.Add_To_End(number)  # here we creating ordered linked list for integer data
        linked.Display()  # here we calling display function  from linked list class
        print()
        while True:
            try:
                number_for_search = int(input("enter your number for search  = "))
                if 0 < number_for_search < 1001:
                    linked.Search_Element_Add_Or_Delete(number_for_search)  # here we calling search function from
                    # linked_list class
                    result = linked.Display_Return()
                    File_Writer("write_data.txt", result)  # file writer function
                    linked.Display()
                    break
                else:
                    print("please enter valid number between 1 to 1000")
            except ValueError:
                print("please enter valid number")

    except FileNotFoundError or ValueError:
        print("please check file path")


if __name__ == '__main__':
    Ordered_Linked_List_Driver()


