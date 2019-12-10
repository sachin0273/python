"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
purpose: in this program we print the calender using stack implemented by linked list
author:  Sachin Shrikant Jadhav
since :  28-08-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""

from data_structure.my_linked_list import Linked_List
from data_structure.calender import Two_D_Array_Calender

linked = Linked_List()


def Stack_Using_Linked():
    """

    :return:this function print the calender using stack

    """
    try:

        stack_calender = [["" for row in range(7)] for column in range(7)]

        result = Two_D_Array_Calender()  # here we calling function from calender.py module for calender

        for index in range(7):  # here we adding in Stack using linked list
            linked.Add_To_Beginning(result[index])

        for row in range(6, -1, -1):  # here we pop from stack and save in 2d array
            result = linked.Delete_At_Beginning_Save()
            stack_calender[row] = result

        for row in range(7):  # here we print the calender from array
            for column in range(7):
                print("{:>2}".format(stack_calender[row][column]), end=" ")
            print()
    except Exception and ValueError as e:
        print(e)


if __name__ == '__main__':
    Stack_Using_Linked()
