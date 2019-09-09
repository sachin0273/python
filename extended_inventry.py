"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we created inventory factory using json file 
author:  Sachin Shrikant Jadhav
since :  5-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
import json


class Inventory_Manager:
    """
    here we created Inventory Manager class
    """

    def _init_(self, inventory_name, quantity):
        """

        :param inventory_name: here we initialize  attribute inventory_name
        :param quantity: here we initialize attribute quantity
        :return: this is a _init_ method hence by using self parameter we access all attributes
        """
        self.inventory_name = inventory_name
        self.quantity = quantity

    def Inventry_Load(self):
        """

        :return: this function read the inventory file and return
        """
        with open('inventry.json', 'r') as outfile:
            data = json.load(outfile)
        return data

    def Inventry_Dump(self, data):
        """

        :param data: here we pass the values to json file
        :return: this function used for writing data into json file

        """
        with open('inventry.json', 'w') as outfile:
            json.dump(data, outfile, indent=2, sort_keys=True)

    def Ask_Inventory(self, inventory):
        """

        :param inventory: here we take inventories in json file
        :param:self.inventory_name:here we take inventory name from user input
        :return: this method validate user input then return inventory name

        """
        while True:
            try:
                self.inventory_name = input("please enter your choice: ")
                if self.inventory_name in inventory:
                    return self.inventory_name
                else:
                    print("please enter inventory from above list")
            except ValueError:
                print("please enter valid input")

    def Ask_Sub_Inventory(self, inventory, main_item):
        """

        :param inventory: this is Ask_Inventory() function returned value
        :param main_item: here we take all inventory details in json file
        :param:inventory_name:here we take sub inventory name
        :return: this method check sub inventory available in inventory or not according return sub inventory name

        """
        while True:
            try:
                self.inventory_name = input("please enter your choice from above list: ")
                for data in main_item[inventory]:
                    if data["name"] == self.inventory_name and self.inventory_name.isalpha():
                        return self.inventory_name
            except ValueError:
                print("please enter valid input")

    def Ask_Quantity(self, inventory, user_inventory, sub_inventory):
        """

        :param inventory: here we take all details of inventory json
        :param user_inventory: this is Ask_Inventory() method returned value
        :param sub_inventory:this is Ask_Sub_Inventory() method returned value
        :param: self.quantity:here we take quantity of item
        :return:this method check quantity available or not according return the quantity

        """
        while True:
            try:
                self.quantity = int(input("please enter quantity"))
                for data in inventory[user_inventory]:
                    if data["name"] == sub_inventory:
                        if int(data["weight"]) > self.quantity > 0:
                            return self.quantity
                        else:
                            print("entered quantity is to large hence enter quantity less than: ", data["weight"])
                            break
            except ValueError:
                print("please enter valid input")

    def Display_Inventry(self, data):
        """

        :param data: here we take all details from inventory json
        :return: this function print the values of inventory

        """
        print("items in inventory : ", end="  ")
        for item in data:
            print(item, end="  ")
        print()

    def Select_Inventry(self, data, user_inventory):
        """

        :param data: here we take all details from inventory json
        :param user_inventory: this is Ask_Inventory() method returned value
        :return: this method according inventory display the sub_inventory in that

        """
        for dat in data[user_inventory]:
            print("item : ", dat["name"], end="   ")
            print("prize_per_kg : ", dat["prize_per_kg"], end="    ,")
        print()

    def Final_Check(self, data, sub_inventory, quantity, inventory):
        """

        :param data: here we take all details from inventory json
        :param sub_inventory: this is Ask_Sub_Inventory() method returned value
        :param quantity: this is Ask_Quantity() method returned value
        :param inventory: this is Ask_Inventory() method returned value
        :return:this method return the updated data to dump into json file

        """
        index_g = 0
        for item in data[inventory]:
            if item["name"] == sub_inventory:
                var = int(item["weight"]) - quantity
                item["weight"] = str(var)
                print(item)
                data[inventory][index_g] = item
            else:
                index_g += 1
        return data


def main():
    while True:
        try:
            operation = int(input("1.continue to inventory\n2.Exit"))  # here we giving options
            if operation == 1 or 2:
                if operation == 1:
                    """
                    below all the methods calling from Inventory_Manager class
                    """
                    store = Inventory_Manager()  # here we creating object of class
                    result = store.Inventry_Load()
                    store.Display_Inventry(result)
                    inventory = store.Ask_Inventory(result)
                    store.Select_Inventry(result, inventory)
                    sub_inventory = store.Ask_Sub_Inventory(inventory, result)
                    quantity = store.Ask_Quantity(result, inventory, sub_inventory)
                    collection = store.Final_Check(result, sub_inventory, quantity, inventory)
                    store.Inventry_Dump(collection)
                elif operation == 2:
                    break
            else:
                print("please enter valid choice")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    main()
