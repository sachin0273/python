from OOPS.commercial_data_processing import Stock_Account
from Utility.utility import load
import json

account = Stock_Account(shares=0, stock_name='')


class Data_Processing:

    def Buy_Share(self, stock_name, share):
        result = load("stock_inventry.json")
        for data in result["Stocks"]:
            if data["stock_name"] == stock_name:
                new_share = int(data["number_of shares"]) - share
                data["number_of shares"] = new_share
        return result

    def Sell_Share(self, stock_name, share):
        result = load("stock_inventry.json")
        for data in result["Stocks"]:
            if data["stock_name"] == stock_name:
                new_share = int(data["number_of shares"]) + share
                data["number_of shares"] = new_share
        return result

    def Driver(self):
        buy_or_sell = int(input("please enter 1 for sell or 2 for buy"))
        if buy_or_sell == 1:
            account.Display()
            stock_name = account.Buy()
            share = account.Shares_For_Buy()
            to_file = self.Buy_Share(stock_name, share)
            with open('stock_inventry.json', 'w') as outfile:
                json.dump(to_file, outfile, indent=2, sort_keys=True)
        elif buy_or_sell == 2:
            account.Display()
            stock_name = account.Sell()
            share = account.Shares_For_Sell()
            to_file=self.Sell_Share(stock_name, share)
            with open('stock_inventry.json', 'w') as outfile:
                json.dump(to_file, outfile, indent=2, sort_keys=True)
        else:
            print("please enter valid input")


if __name__ == '__main__':
    Data_Processing().Driver()
