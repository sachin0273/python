"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we create stock account name mobile number and replace in message,
         and print the replaced string massage
author:  Sachin Shrikant Jadhav
since :  6-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""

from Utility.utility import load


class Stock_Account:
    """
    here we created class Stock Account

    """
    def __init__(self, shares, stock_name):
        """

        :param shares: here we initialize the attribute shares
        :param stock_name: here we initialize attribute stock_name

        """
        self.shares = shares
        self.stock_name = stock_name

    def Buy(self, stocks):
        """

        :param stocks: here we take all details in stock json file
        :return: this method return the stock name want to buy

        """
        while True:
            try:
                self.stock_name = input("please enter your stock name want to buy from above list")
                for index in stocks["Stocks"]:
                    if index["stock_name"] == self.stock_name:
                        return self.stock_name
            except ValueError:
                print("please enter valid  name")

    def Sell(self, stocks):
        """

        :param stocks: here we take all details in stock json file
        :return: this method return stock name want sell

        """
        while True:
            try:
                self.stock_name = input("please enter your stock name want to buy from above list ")
                for index in stocks["Stocks"]:
                    if index["stock_name"] == self.stock_name:
                        return self.stock_name
            except ValueError:
                print("please enter valid  name")

    def Shares_For_Buy(self):
        """

        :return: this method return the number of shares want to buy

        """
        while True:
            try:
                self.shares = int(input("please enter number of shares you want to buy"))
                if 0 < self.shares < 1001:
                    return self.shares
                else:
                    print("please enter valid shares less than 1000")
            except ValueError:
                print("please enter valid input")

    def Shares_For_Sell(self, stocks, stock_name):
        """

        :param stocks: here we take all details in stock json file
        :param stock_name: this value is returned by Sell() method
        :return: this method check the shares according to stock name and then return the value of shares

        """
        while True:
            try:
                self.shares = int(input("please enter number of shares you want to sell"))
                for index in stocks["Stocks"]:
                    if index["stock_name"] == stock_name:
                        if index["number_of shares"] > self.shares > 0:
                            return self.shares
                        else:
                            print("please enter valid shares less than", index["number_of shares"])
                            break
            except ValueError:
                print("please enter valid input")

    def Display(self):
        """

        :return: this method display the all stock from json file

        """
        data = load("stock_inventry.json")
        for index in data["Stocks"]:
            print("stock", "shares", "price")
            print("{:>2}".format(index["stock_name"]), end="  ")
            print("{:>2}".format(index["number_of shares"]), end="  ")
            print("{:>2}".format(index["price"]))
            print()


if __name__ == '__main__':
    Stock_Account()
