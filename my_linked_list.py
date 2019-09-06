<<<<<<< HEAD
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Purpose: it is linked_list Class where logic of all linked list methods are written .
         This is done so most of the code can be reused
author:  Sachin Shrikant Jadhav
since :  26-08-2019

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from data_structure.Node import Node

""" from here start the linked list class where all methods written"""


class Linked_List:
    """
    here is constructor of the linked list
    """

    def __init__(self, head=None):
        self.head = head

    def Add_To_Beginning(self, data):
        """
        :param data: here we pass the user data will be add in new node
        :return: this method gives new node ahead of head node

        """
=======
from data_structure.Node import Node


class linked_list:
    def __init__(self, head=None):
        self.head = head

    def add_to_start(self, data):
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

<<<<<<< HEAD
    def Delete_From_Beginning(self):
        """

        :return: this method used for delete or remove first node in the linked list

        """
        if self.head is None:
            print("empty")
        else:
            self.head = self.head.next

    def Delete_At_End(self):
        """

        :return: in this method we remove the node from last

        """
        global delete
        delete = self.head
=======
    def delete_to_start(self):
        self.head = self.head.next

    def delete_to_last(self):
        global delete
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
        temp = self.head
        if temp is None:
            print("linked list is empty")
        else:
            while temp.next is not None:
                delete = temp
                temp = temp.next
            delete.next = None

<<<<<<< HEAD
    def Add_To_End(self, data):
        """

        :param data:here we pass the user data to the this function
        :return: this function is used for add user data at the end of linked list

        """
        new_node = Node(data)
        temp = self.head
        if temp is None:
            self.Add_To_Beginning(data)
=======
    def add_to_last(self, data):
        new_node = Node(data)
        temp = self.head
        if temp is None:
            self.add_to_start(data)
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

<<<<<<< HEAD
    def Display(self):
        """

        :return: this method is used for display all data in linked list

        """
=======
    def display(self):
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

<<<<<<< HEAD
    def Search(self, search_element):
        """

        :param search_element: here we pass element for search in linked list
        :return: this method is used for if element found return true or false

        """
=======
    def search(self, search_element):
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
        flag = 0
        temp = self.head
        if temp is None:
            print("linked list empty")
        else:
            while temp is not None:
                if temp.data == search_element:
                    print("element found")
                    flag = 1
                    break
                else:
                    temp = temp.next
            if flag == 0:
                print("element not found")

<<<<<<< HEAD
    def Delete_At_Position(self, position):
        """

        :param position: here we pass position in the linked list
        :return:  this function used for remove the node on the position

        """
=======
    def delete_at_position(self, position):
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
        temp = self.head
        if temp is None:
            print("linked list empty ")
        else:
            for i in range(position - 1):
                temp = temp.next
            new = temp.next.next
            temp.next = new

<<<<<<< HEAD
    def Insert_At_Position(self, position, data):
        """

        :param position: here we pass position of new_node in linked list
        :param data: here we pass data of new_node
        :return:this function is used for insert the new_node at given position

        """
=======
    def insert_at_position(self, position, data):
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
        temp = self.head
        new_node = Node(data)
        if temp is None:
            print("linked list is empty we adding node at start")
<<<<<<< HEAD
            self.Add_To_Beginning(data)  # here we calling add to start method from same class
=======
            self.add_to_start(data)
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
        else:
            for i in range(position - 1):
                temp = temp.next
            next_link = temp.next
            temp.next = new_node
            new_node.next = next_link

<<<<<<< HEAD
    def Search_Element_Add_Or_Delete(self, search_element):
        """

        :param search_element: here we pass the data for search in linked list
        :return: in this function if user input data find in linked list then is removed else added in linked list

        """
=======
    def search_element_add_delete(self, search_element):
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
        flag = 0
        count = 0
        temp = self.head
        if temp is None:
            print("linked list empty")
<<<<<<< HEAD
        elif temp.data == search_element:
            self.Delete_From_Beginning()  # here we calling delete to start method from same class
        else:
            while temp is not None:
                if temp.data == search_element:
                    self.Delete_At_Position(count)  # here we calling delete at position method from same class
=======
        else:
            while temp is not None:
                if temp.data == search_element:
                    self.delete_at_position(count)
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
                    flag = 0
                    break
                else:
                    temp = temp.next
                    count += 1
                    flag = 1
            if flag == 1:
<<<<<<< HEAD
                self.Add_To_End(search_element)  # here we calling add to last method from same class

    def Delete_To_Last_Save(self):
        """
        :purpose: here method is used for Queue
        :return: this function used for delete last Node  and return that data on deleted Node

        """
=======
                self.add_to_last(search_element)

    def delete_to_last_save(self):
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
        global delete
        temp = self.head
        if temp is None:
            print("linked list is empty")
<<<<<<< HEAD
        elif temp.next is not None:
            while temp.next.next is not None:
                temp = temp.next
            value = temp.next.data
            temp.next = None
            return value
        else:
            return self.Delete_At_Beginning_Save()

    def Delete_At_Beginning_Save(self):
        """

        :return: this function used for delete first Node and return data on that node

        """
        temp = self.head
        self.head = self.head.next
        return temp.data

    def Display_Return(self):
        display = []
        temp = self.head
        while temp is not None:
            display.append(temp.data)
            temp = temp.next
        return display


if __name__ == '__main__':
    Linked_List()
=======
        else:
            while temp is not None:
                delete = temp
                temp = temp.next

            delete = None
            return delete.data

    def delete_to_start_save(self):
        temp = self.head
        self.head = self.head.next
        return temp.data
>>>>>>> fe6d22f571df9e3d6857feef5e77c3b553d9cb95
