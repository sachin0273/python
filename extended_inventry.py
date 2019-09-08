import json


class Inventory_Manager:
    def _init_(self, inventry_name, quntity):
        self.inventry_name = inventry_name
        self.quntity = quntity

    def Inventry_Load(self):
        with open('inventry.json', 'r') as outfile:
            data = json.load(outfile)
        return data

    def Inventry_Dump(self, data):
        with open('inventry.json', 'w') as outfile:
            json.dump(data, outfile, indent=2, sort_keys=True)

    def Ask_Inventory(self, inventory):
        while True:
            try:
                self.inventry_name = input("please enter your choice: ")
                if self.inventry_name in inventory:
                    return self.inventry_name
                else:
                    print("please enter inventory from above list")
            except ValueError:
                print("please enter valid input")

    def Ask_Sub_Inventory(self, inventory, main_item):
        while True:
            try:
                self.inventry_name = input("please enter your choice from above list: ")
                for data in main_item[inventory]:
                    if data["name"] == self.inventry_name and self.inventry_name.isalpha():
                        return self.inventry_name
            except ValueError:
                print("please enter valid input")

    def Ask_Quntity(self, inventory, user_inventory, sub_inventory):
        while True:
            try:
                self.quntity = int(input("please enter quantity"))
                for data in inventory[user_inventory]:
                    if data["name"] == sub_inventory:
                        if int(data["weight"]) > self.quntity > 0:
                            return self.quntity
                        else:
                            print("entered quantity is to large hence enter quantity less than: ", data["weight"])
                            break
            except ValueError:
                print("please enter valid input")

    def Display_Inventry(self, data):
        print("items in inventory : ", end="  ")
        for p in data:
            print(p, end="  ")
        print()

    def Select_Inventry(self, data, user_inventry):
        for dat in data[user_inventry]:
            print("item : ", dat["name"], end="   ")
            print("prize_per_kg : ", dat["prize_per_kg"], end="    ,")
        print()

    def Final(self, data, item, qunt, mj):
        g = 0
        for h in data[mj]:
            if h["name"] == item:
                var = int(h["weight"]) - qunt
                h["weight"] = str(var)
                print(h)
                data[mj][g] = h
            else:
                g += 1
        return data


def main():
    while True:
        try:
            operation = int(input("1.continue to inventory\n2.Exit"))
            if operation == 1 or 2:
                if operation == 1:
                    store = Inventory_Manager()
                    result = store.Inventry_Load()
                    store.Display_Inventry(result)
                    inventory = store.Ask_Inventory(result)
                    store.Select_Inventry(result, inventory)
                    sub_inventory = store.Ask_Sub_Inventory(inventory, result)
                    quantity = store.Ask_Quntity(result, inventory, sub_inventory)
                    collection = store.Final(result, sub_inventory, quantity, inventory)
                    store.Inventry_Dump(collection)
                elif operation == 2:
                    break
            else:
                print("please enter valid choice")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    main()
