"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we create the balnced parentheses for mathematical expressions in this we creating stack using
         linked list for e.g push open parenthesis “(“ and pop parenthesis “)”.
author:  Sachin Shrikant Jadhav
since :  26-08-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

from data_structure.my_linked_list import Linked_List

""" here we creating object"""

linked = Linked_List()


def Balanced_Parentheses():
    """

    :return: in this function we take user input mathematical expression and return the expression balnced or not

    """
    while True:
        try:
            flag = 1
            expression = input("please enter your   expression ")
            for parenthesis in expression:
                if parenthesis == "(":
                    linked.Add_To_Beginning(parenthesis)
                elif parenthesis == ")":
                    if linked.head is None:
                        flag = 2
                    else:
                        linked.Delete_From_Beginning()  # here we calling function from linked list class
                else:
                    print("please enter valid parenthesises in () bracket ")
                    flag = 0
                    break
            if flag == 1 and linked.head is None:
                print("it is balnced parenthesis")
                break
            elif flag == 1 and linked.head is not None:
                print("it is not balanced")
                break
            elif flag == 2:
                print("this expression not balanced")
                break
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Balanced_Parentheses()

