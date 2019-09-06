<<<<<<< HEAD
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
purpose: in this program we creates Banking Cash Counter where people come in to deposit Cash and withdraw Cash
         and maintaining the cash balance
author:  Sachin Shrikant Jadhav
since :  26-08-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""

from data_structure.my_linked_list import Linked_List

""" here we creating object """

linked = Linked_List()
=======
from data_structure.my_linked_list import linked_list

linked = linked_list()
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95

bank_amount = 40000


<<<<<<< HEAD
def Banking_Cash_Counter_Driver():
    """

    :purpose: here we creating program using Queue by linked list
    :return: this function return banking cash counter

    """
    global bank_amount
    while True:
        try:
            people_in_queue = int(input("please enter number of people in queue"))
            if people_in_queue < 100:
                while True:
                    flag = 1
                    for people in range(people_in_queue):
                        people_name = input("enter name of people in queue")
                        if people_name.isalpha():
                            linked.Add_To_Beginning(people_name)  # here we calling Queue method from linked list
                        else:
                            flag = 0
                            print("please enter valid input and name length less than 7")
                            break
                    if flag == 1:
                        print("enqueue completed")
                        break

                for people in range(people_in_queue):
                    linked.Display()  # here we calling display display from linked list class
                    print()
                    deposit_or_withdraw = int(input("if you want to deposit please enter 1 or if you want withdraw \
                        please enter 0"))
                    while 0 < deposit_or_withdraw > 1:
                        deposit_or_withdraw = int(input("if you want to deposit please enter 1 or if you want withdraw \
                                                please enter 0"))
                    if deposit_or_withdraw == 1:
                        while True:
                            try:
                                deposit = int(input("enter your amount for deposit"))
                                bank_amount = bank_amount + deposit
                                linked.Delete_At_End()  # here we calling deque method from linked list
                                break
                            except ValueError:
                                print("please enter valid input")
                    elif deposit_or_withdraw == 0:
                        while True:
                            try:
                                withdraw = int(input("enter your amount"))
                                while withdraw > bank_amount:
                                    print("enter amount is two large")
                                    withdraw = int(input("please enter amount again "))

                                bank_amount = bank_amount - withdraw

                                linked.Delete_At_End()
                                break
                            except ValueError:
                                print("please enter valid input")
                print("deque completed")
                break
            else:
                print("please enter valid input")

        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Banking_Cash_Counter_Driver()
=======
def banking_cash_counter_driver():
    global bank_amount
    people_in_queue = int(input("please enter number of people in queue"))
    for i in range(people_in_queue):
        people_name = input("enter name of people in queue")
        linked.add_to_start(people_name)
    print("enqueue completed")
    for i in range(people_in_queue):
        linked.display()
        print()
        deposit_or_withdraw = int(input("if you want to deposit please enter 1 or if you want withdraw please enter 0"))
        if deposit_or_withdraw == 1:
            deposit = int(input("enter your amount"))
            bank_amount = bank_amount + deposit
            linked.delete_to_last()
        elif deposit_or_withdraw == 0:
            withdraw = int(input("enter your amount"))
            while withdraw > bank_amount:
                print("enter amount is two large")
                withdraw=int(input("please enter amount again "))

            bank_amount = bank_amount - withdraw

            linked.delete_to_last()
    print("deque completed")


if __name__ == '__main__':
    banking_cash_counter_driver()
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
