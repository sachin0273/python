"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
purpose: in this program we print the anagram using queue implemented by linked list
author:  Sachin Shrikant Jadhav
since :  28-08-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

from data_structure.my_linked_list import Linked_List
from data_structure.prime_anagram_array import Prime_Array

"""here we creating object"""
linked = Linked_List()


def Anagram_Queue():
    """

    :return: in this function we print prime anagrams between 1 to 1000 numbers

    """
    try:
        anagrams = Prime_Array()  # here we calling anagram array from prime_anagram.py module

        for i in anagrams[0]:  # here we adding anagram in queue linked list
            linked.Add_To_Beginning(i)  # here we calling function from linked list
        while linked.head.next is not None:  # here we printing anagram from queue
            result = linked.Delete_To_Last_Save()  # calling function from linked list
            print(result, end=" ")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    Anagram_Queue()
