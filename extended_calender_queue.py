"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
purpose: in this program we creating the queue using linked list for calender
author:  Sachin Shrikant Jadhav
since :  27-08-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

from data_structure.my_linked_list import Linked_List
from data_structure.calender import Two_D_Array_Calender

""" here we  creating object"""
linked = Linked_List()


def Extended_Calender_Queue():
    """

    :return:this function return the the calender from queue using linked list

    """
    try:
        result = Two_D_Array_Calender()  # here we calling calender from calender module

        for row in range(7):
            for column in range(7):
                linked.Add_To_Beginning(result[row][column])  # here we enque calender row by row

            while linked.head is not None:  # here we deque calender row by row
                element = linked.Delete_To_Last_Save()
                print("{:>2}".format(element), end=" ")
            print()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    Extended_Calender_Queue()
