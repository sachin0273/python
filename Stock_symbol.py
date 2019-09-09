"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we maintain stock symbol in stack implemented by linked list 
author:  Sachin Shrikant Jadhav
since :  7-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
from Utility.utility import load
from data_structure.my_linked_list import Linked_List
from OOPS.data_processing import Data_Processing
from OOPS.commercial_data_processing import Stock_Account
import json

account = Stock_Account(shares=None, stock_name='')
"""here we creating object of imported Stock account class"""

share = Data_Processing()
"""here we creating object of imported Data processing class"""

linked = Linked_List()
"""here we creating object of Linked List class"""


class Stack_Linked_List:
    """ here we created class Stack_Linked_List"""

    def Buy_Share(self, stock_name, share):
        """
        :param stock_name: this is stock name you want buy
        :param share: this number of shares you want to buy
        :return:this method update the stock account after every buy operation
        """
        result = load("stock_inventry.json")
        for data in result["Stocks"]:
            if data["stock_name"] == stock_name:
                new_share = int(data["number_of shares"]) + share
                data["number_of shares"] = new_share
        return result

    def Sell_Share(self, stock_name, share):
        """
        :param stock_name: this is stock name you want sell
        :param share: this number of shares you want to sell
        :return:this method update the stock account after every sell operation
        """
        result = load("stock_inventry.json")
        for data in result["Stocks"]:
            if data["stock_name"] == stock_name:
                new_share = int(data["number_of shares"]) - share
                data["number_of shares"] = new_share
        return result

    def All_Stocks(self):
        """
        :return: this method return all stock details
        """
        stocks = load("stock_inventry.json")
        return stocks

    def Stack(self):
        """

        :return: in this method we actual perform the stock account and write the operations into jason file
                 and every operation of sell or buy maintain the stock symbol in stack implemented by linked list
        """
        while True:
            while True:
                try:
                    print("please enter your choice")
                    buy_or_sell = int(input("1.buy\n2.sell\n3.Exit\n "))
                    if buy_or_sell == 1:
                        account.Display()
                        stock = self.All_Stocks()
                        stock_name = account.Buy(stock)
                        share = account.Shares_For_Buy()
                        to_file = self.Buy_Share(stock_name, share)
                        linked.Add_To_Beginning(stock_name)
                        with open('stock_inventry.json', 'w') as outfile:
                            json.dump(to_file, outfile, indent=2, sort_keys=True)
                        print("successfully shares bought and stock name added in Stack")
                        print()
                    elif buy_or_sell == 2:
                        account.Display()
                        stock = self.All_Stocks()
                        stock_name = account.Sell(stock)
                        share = account.Shares_For_Sell(stock, stock_name)
                        to_file = self.Sell_Share(stock_name, share)
                        linked.Add_To_Beginning(stock_name)
                        with open('stock_inventry.json', 'w') as outfile:
                            json.dump(to_file, outfile, indent=2, sort_keys=True)
                        print("successfully shares sold and stock name added in Stack")
                        print()
                    elif buy_or_sell == 3:
                        print("your last transactions")
                        linked.Display()
                        return
                    else:
                        print("please enter valid choice")
                except ValueError:
                    print("please enter valid input")


if __name__ == '__main__':
    Stack_Linked_List().Stack()
