from OOPS.commercial_data_processing import Stock_Account
from Utility.utility import load
import json

account = Stock_Account(shares=0, stock_name='')


class Data_Processing:

    def Buy_Share(self, stock_name, share):
        result = load("stock_inventry.json")
        for data in result["Stocks"]:
            if data["stock_name"] == stock_name:
                new_share = int(data["number_of shares"]) + share
                data["number_of shares"] = new_share
        return result

    def Sell_Share(self, stock_name, share):
        result = load("stock_inventry.json")
        for data in result["Stocks"]:
            if data["stock_name"] == stock_name:
                new_share = int(data["number_of shares"]) - share
                data["number_of shares"] = new_share
        return result

    def All_Stocks(self):
        stocks = load("stock_inventry.json")
        return stocks

    def Driver(self):
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
                    with open('stock_inventry.json', 'w') as outfile:
                        json.dump(to_file, outfile, indent=2, sort_keys=True)
                    print("successfully shares bought")
                    print()
                elif buy_or_sell == 2:
                    account.Display()
                    stock = self.All_Stocks()
                    stock_name = account.Sell(stock)
                    share = account.Shares_For_Sell(stock,stock_name)
                    to_file = self.Sell_Share(stock_name, share)
                    with open('stock_inventry.json', 'w') as outfile:
                        json.dump(to_file, outfile, indent=2, sort_keys=True)
                    print("successfully shares sold")
                    print()
                elif buy_or_sell == 3:
                    break
                else:
                    print("please enter valid choice")
            except ValueError:
                print("please enter valid input")


if __name__ == '__main__':
    Data_Processing().Driver()
