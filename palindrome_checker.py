<<<<<<< HEAD
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
purpose: in this program we check the palindrome using deque
author:  Sachin Shrikant Jadhav
since :  26-08-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

from data_structure.my_linked_list import Linked_List

"""here we creating object"""
linked = Linked_List()

word = ""


def Palindrome_Driver():
    """
    :param:string: here we get string for checking palindrome
    :return: this function we enqueue and deque the string from rear and check is palindrome or not

    """
    global word
    while True:
        try:
            string = input("please enter your string")
            if string.isalpha() and len(string) < 11:
                for char in string:
                    linked.Add_To_Beginning(char)  # this function for adding rear and calling from linked list class
                print()

                for char in range(len(string)):
                    result = linked.Delete_At_Beginning_Save()  # this function for deque string from rear and calling
                    # from linked list
                    word = word + result

                if word == string:
                    print("is palindrome")

                else:
                    print("is not palindrome")
                break
            else:
                print("please enter char an length less than 11")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Palindrome_Driver()
=======
from data_structure.my_linked_list import linked_list

linked = linked_list()

global word
word = ""


def palindrome_driver():
    global word
    string = input("please enter your string")

    for i in string:
        linked.add_to_start(i)
    linked.display()
    print()
    for i in range(len(string)):
        result = linked.delete_to_start_save()
        word = word + result
    if word == string:
        print("is palindrome")
    else:
        print("is not palindrome")


if __name__ == '__main__':
    palindrome_driver()
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
