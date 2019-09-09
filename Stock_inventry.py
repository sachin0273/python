"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we read the stock inventory json file and print the values in json
author:  Sachin Shrikant Jadhav
since :  4-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
import json


class Stock:
    """here we created class of Stock"""

    def Each_Stock_Value(self):
        """
        :purpose:this function used for read the stock inventory json file and read each stock in the file
        :return:this function return or print each stock value in the stock_inventory json

        """
        try:
            with open('stock_inventry.json', 'r') as outfile:  # here we reading the json file
                data = json.load(outfile)
            for item in data:
                for stock in data[item]:
                    print("stock value of", stock["stock_name"], "is :")
                    print(int(stock["price"]) * int(stock["number_of shares"]))
                    print()
        except FileNotFoundError:
            print("please check the file path")

    def Total_Stock_Value(self):
        """

        :return:this function used for reading the each stock value in json file and pint the total stock value

        """
        total_stack_value = 0
        try:
            with open('stock_inventry.json', 'r') as outfile:  # here we reading json file
                data = json.load(outfile)
            for item in data:
                for stock in data[item]:
                    total_stack_value = total_stack_value + int(stock["price"]) * int(stock["number_of shares"])
            print("total stock value is =  ", total_stack_value)
        except FileNotFoundError:
            print("please check file path")


if __name__ == '__main__':
    details = Stock()
    print(details.Each_Stock_Value())
    print(details.Total_Stock_Value())
