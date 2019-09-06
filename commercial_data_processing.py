from Utility.utility import load


class Stock_Account:
    def __init__(self, shares, stock_name):
        self.shares = shares
        self.stock_name = stock_name

    def Buy(self):
        self.stock_name = input("please enter your stock name want to buy ")
        return self.stock_name

    def Sell(self):
        self.stock_name = input("please enter your stock name want to sell")
        return self.stock_name

    def Shares_For_Buy(self):
        self.shares = int(input("please enter number of shares you want to buy"))
        return self.shares

    def Shares_For_Sell(self):
        self.shares = int(input("please enter number of shares you want to sell"))
        return self.shares

    def Display(self):
        data = load("stock_inventry.json")
        for i in data["Stocks"]:
            print("stock", "shares", "price")
            print("{:>2}".format(i["stock_name"]), end="  ")
            print("{:>2}".format(i["number_of shares"]), end="  ")
            print("{:>2}".format(i["price"]))
            print()
        print()


if __name__ == '__main__':
    Stock_Account()
