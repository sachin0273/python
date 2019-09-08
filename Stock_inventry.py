import json


class Stock:
    def Each_Stock_Value(self):
        try:
            with open('stock_inventry.json', 'r') as outfile:
                data = json.load(outfile)
            for i in data:
                for dat in data[i]:
                    print("stock value of", dat["stock_name"], "is :")
                    print(int(dat["price"]) * int(dat["number_of shares"]))
                    print()
        except FileNotFoundError:
            print("please check the file path")

    def Total_Stock_Value(self):
        total_stack_value = 0
        try:
            with open('stock_inventry.json', 'r') as outfile:
                data = json.load(outfile)
            for i in data:
                for dat in data[i]:
                    total_stack_value = total_stack_value + int(dat["price"]) * int(dat["number_of shares"])
            print("total stock value is =  ", total_stack_value)
        except FileNotFoundError:
            print("please check file path")


if __name__ == '__main__':
    details = Stock()
    print(details.Each_Stock_Value())
    print(details.Total_Stock_Value())
