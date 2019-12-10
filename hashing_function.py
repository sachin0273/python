"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
purpose: in this program we read the integer from file and create the chain of number depending upon their slot
        slot is based on reminder of number after dividing by 11
author:  Sachin Shrikant Jadhav
since :  27-08-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

from data_structure.my_linked_list import Linked_List
from Utility.utility import File_Int_Reader


def Hash_Function_Driver():
    """

    :return: this function return the hash_list of integers

    """
    try:
        hash_list = []
        for index in range(11):
            hash_list.append(Linked_List())  # here we creating 10 different object for each slot

        result = File_Int_Reader("data_int_data.txt")
        for number in result:
            space = number % 11
            """ 
            here we adding element to the linked list based on reminder of number using 
            add to start function called from linked list
            """
            hash_list[space].Add_To_Beginning(number)
        while True:
            try:
                number_for_search = int(input(" please enter number for search "))
                if 0 < number_for_search < 1000:
                    element = number_for_search % 11
                    hash_list[element].Search_Element_Add_Or_Delete(number_for_search)  # here we calling function for
                    # search in linked list
                    break
                else:
                    print("please enter number between 1 to 1000")
            except ValueError:
                print("please enter valid input")

        print(hash_list)
        index = 0
        for data in hash_list:
            print("position-->{}".format(index), end=' ')
            data.Display()
            print()
            index += 1
    except FileNotFoundError:
        print("please enter valid file path")


if __name__ == '__main__':
    Hash_Function_Driver()
