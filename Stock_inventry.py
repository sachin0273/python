import json


class Stock:
    def __init__(self):
        self

    def each_stock_value(self):
        with open('stock_inventry.json', 'r') as outfile:
            data = json.load(outfile)
        for i in data:
            for dat in data[i]:
                print("stock value of", dat["stock_name"], "is :")
                print(int(dat["price"]) * int(dat["number_of shares"]))
                print()

    def total_stock_value(self):
        total_stack_value = 0
        with open('stock_inventry.json', 'r') as outfile:
            data = json.load(outfile)
        for i in data:
            for dat in data[i]:
                total_stack_value = total_stack_value + int(dat["price"]) * int(dat["number_of shares"])
        print("total stock value is =  ", total_stack_value)


if __name__ == '__main__':
    s1 = Stock()
    print(s1.each_stock_value())
    print(s1.total_stock_value())
