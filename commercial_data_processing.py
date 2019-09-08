from Utility.utility import load


class Stock_Account:
    def __init__(self, shares, stock_name):
        self.shares = shares
        self.stock_name = stock_name

    def Buy(self, stocks):
        while True:
            try:
                self.stock_name = input("please enter your stock name want to buy from above list")
                for index in stocks["Stocks"]:
                    if index["stock_name"] == self.stock_name:
                        return self.stock_name
            except ValueError:
                print("please enter valid  name")

    def Sell(self, stocks):
        while True:
            try:
                self.stock_name = input("please enter your stock name want to buy from above list ")
                for index in stocks["Stocks"]:
                    if index["stock_name"] == self.stock_name:
                        return self.stock_name
            except ValueError:
                print("please enter valid  name")

    def Shares_For_Buy(self):
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
        data = load("stock_inventry.json")
        for index in data["Stocks"]:
            print("stock", "shares", "price")
            print("{:>2}".format(index["stock_name"]), end="  ")
            print("{:>2}".format(index["number_of shares"]), end="  ")
            print("{:>2}".format(index["price"]))
            print()


if __name__ == '__main__':
    Stock_Account()
