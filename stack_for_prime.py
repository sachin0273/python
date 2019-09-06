"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

purpose: in this program we adding anagram between 1 to 1000 into stack and printing in reverse order
author:  Sachin Shrikant Jadhav
since :  29-08-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

from data_structure.my_linked_list import Linked_List
from data_structure.prime_anagram_array import Prime_Array

""" here we creating object"""
linked = Linked_List()


def Stack_Prime():
    """

    :return: this function add anagram number in stack and print in reverse order


    """
    try:
        anagrams = Prime_Array()  # here we calling prime array function for anagrams
        for anagram in anagrams[0]:
            linked.Add_To_Beginning(anagram)  # here we calling add_start function from linked list
        linked.Display()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    Stack_Prime()
