from data_structure.Node import Node

""" from here start the linked list class where all methods written"""


class linked_test:
    """
    here is constructor of the linked list
    """

    def __init__(self, head=None):
        self.head = head

    def add_to_start(self, data):
        """
        :param data: here we pass the user data will be add in new node
        :return: this method gives new node ahead of head node

        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_to_start(self):
        """

        :return: this method used for delete or remove first node in the linked list

        """
        self.head = self.head.next

    def delete_to_last(self):
        """

        :return: in this method we remove the node from last

        """
        global delete
        temp = self.head
        if temp is None:
            print("linked list is empty")
        else:
            while temp.next is not None:
                delete = temp
                temp = temp.next
            delete.next = None

    def add_to_last(self, data):
        """

        :param data:here we pass the user data to the this function
        :return: this function is used for add user data at the end of linked list

        """
        new_node = Node(data)
        temp = self.head
        if temp is None:
            self.add_to_start(data)
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def display(self):
        """

        :return: this method is used for display all data in linked list

        """
        display = []
        temp = self.head
        while temp is not None:
            display.append(temp.data)
            temp = temp.next
        return display

    def search(self, search_element):
        """

        :param search_element: here we pass element for search in linked list
        :return: this method is used for if element found return true or false

        """
        flag = 0
        temp = self.head
        if temp is None:
            print("linked list empty")
        else:
            while temp is not None:
                if temp.data == search_element:
                    print("element found")
                    flag = 1
                    return True
                else:
                    temp = temp.next
            if flag == 0:
                print("element not found")
                return False
    def delete_at_position(self, position):
        """

        :param position: here we pass position in the linked list
        :return:  this function used for remove the node on the position

        """
        temp = self.head
        if temp is None:
            print("linked list empty ")
        else:
            for i in range(position - 1):
                temp = temp.next
            new = temp.next.next
            temp.next = new

    def insert_at_position(self, position, data):
        """

        :param position: here we pass position of new_node in linked list
        :param data: here we pass data of new_node
        :return:this function is used for insert the new_node at given position

        """
        temp = self.head
        new_node = Node(data)
        if temp is None:
            print("linked list is empty we adding node at start")
            self.add_to_start(data)  # here we calling add to start method from same class
        else:
            for i in range(position - 1):
                temp = temp.next
            next_link = temp.next
            temp.next = new_node
            new_node.next = next_link

    def search_element_add_delete(self, search_element):
        """

        :param search_element: here we pass the data for search in linked list
        :return: in this function if user input data find in linked list then is removed else added in linked list

        """
        flag = 0
        count = 0
        temp = self.head
        if temp is None:
            print("linked list empty")
        elif temp.data == search_element:
            self.delete_to_start()  # here we calling delete to start method from same class
        else:
            while temp is not None:
                if temp.data == search_element:
                    self.delete_at_position(count)  # here we calling delete at position method from same class
                    flag = 0
                    break
                else:
                    temp = temp.next
                    count += 1
                    flag = 1
            if flag == 1:
                self.add_to_last(search_element)  # here we calling add to last method from same class

    def delete_to_last_save(self):
        """
        :purpose: here method is used for Queue
        :return: this function used for delete last Node  and return that data on deleted Node

        """
        global delete
        temp = self.head
        if temp is None:
            print("linked list is empty")
        elif temp.next is not None:
            while temp.next.next is not None:
                temp = temp.next
            value = temp.next.data
            temp.next = None
            return value
        else:
            return self.delete_to_start_save()

    def delete_to_start_save(self):
        """

        :return: this function used for delete first Node and return data on that node

        """
        temp = self.head
        self.head = self.head.next
        return temp.data


if __name__ == '__main__':
    linked_test()
