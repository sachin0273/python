from Utility.utility import load
from data_structure.my_linked_list import Linked_List
from OOPS.data_processing import Data_Processing
from OOPS.commercial_data_processing import Stock_Account
import json

account = Stock_Account(shares=None, stock_name='')
share = Data_Processing()
linked = Linked_List()


class Stack_Linked_List:

    def Buy_Share(self, stock_name, shares):
        result = load("stock_inventry.json")
        for data in result["Stocks"]:
            if data["stock_name"] == stock_name:
                new_share = int(data["number_of shares"]) + shares
                data["number_of shares"] = new_share
        return result

    def Sell_Share(self, stock_name, shares):
        result = load("stock_inventry.json")
        for data in result["Stocks"]:
            if data["stock_name"] == stock_name:
                new_share = int(data["number_of shares"]) - shares
                data["number_of shares"] = new_share
        return result

    def Stack(self):
        while True:
            buy_or_sell = int(input("please enter 1 for buy and 2 for sell""for exit enter 3"))
            if buy_or_sell == 2:
                account.Display()
                stock_name = input("please enter stock name to sell")
                number_of_share = int(input("please enter number of shares"))
                to_file = self.Sell_Share(stock_name, number_of_share)
                linked.Add_To_Beginning(stock_name)
                print()
                with open('stock_inventry.json', 'w') as outfile:
                    json.dump(to_file, outfile, indent=2, sort_keys=True)
            elif buy_or_sell == 1:
                account.Display()
                stock_name = input("please enter stock name to buy")
                number_of_share = int(input("please enter number of shares"))
                to_file = self.Buy_Share(stock_name, number_of_share)
                linked.Add_To_Beginning(stock_name)
                print()
                with open('stock_inventry.json', 'w') as outfile:
                    json.dump(to_file, outfile, indent=2, sort_keys=True)
            if buy_or_sell == 3:
                print("last transactions")
                linked.Display()
                break


if __name__ == '__main__':
    Stack_Linked_List().Stack()
