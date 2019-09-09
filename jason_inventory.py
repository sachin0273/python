"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we read the inventory json file and print the values in inventory
author:  Sachin Shrikant Jadhav
since :  4-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""

import json


class Inventory:
    """here we created class Inventory """

    def Load_Inventery_From_File(self):
        """

        :return: here we read the inventory json file and return data in jason file

        """
        with open('inventry.json', 'r') as outfile:
            inventory = json.load(outfile)
            return inventory

    def Display_Value(self, inventory):
        """

        :param inventory: here we take return data of inventory file
        :return: in this function we print the values in json inventory file

        """
        for data in inventory:
            print("{:>7}".format(data), " ""quantity", " ""price_per_kg")
            for item in range(len(inventory[data])):
                for value in inventory[data][item].values():  # here we getting all values from json
                    print("{:>7}".format(value), end=" ")
                print()
            print()


if __name__ == '__main__':
    inventory = Inventory()
    result = inventory.Load_Inventery_From_File()
    inventory.Display_Value(result)  # here we Displaying values in inventory
