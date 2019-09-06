import json


class inventryManager:
    def _init_(self, inventry_name, quntity):
        self.inventry_name = inventry_name
        self.quntity = quntity

    def load(self):
        with open('inventry.json', 'r') as outfile:
            data = json.load(outfile)
        return data

    def dump(self, data):
        with open('inventry.json', 'w') as outfile:
            json.dump(data, outfile, indent=2, sort_keys=True)

    def ask_inventry(self):
        self.inventry_name = input("please enter your choice : ")
        return self.inventry_name

    def ask_quntity(self):
        self.quntity = int(input("please enter quantity"))
        return self.quntity

    def display_inventry(self, data):
        print("items in inventory : ", end="  ")
        for p in data:
            print(p, end="  ")
        print()

    def select_inventry(self, data, user_inventry):
        if user_inventry not in data:
            print("enter valid input")
            return
        for dat in data[user_inventry]:
            print("item : ", dat["name"], end="   ")
            print("prize_per_kg : ", dat["prize_per_kg"], end="    ,")
        print()

    def final(self, data, item, qunt, mj):
        g = 0
        for h in data[mj]:
            if h["name"] == item:
                var = int(h["weight"]) - qunt
                h["weight"] = str(var)
                print(h)
                data[mj][g] = h
                print(data[mj])
            else:
                g += 1
        return data


if __name__ == '__main__':
    s1 = inventryManager()
    result = s1.load()
    s1.display_inventry(result)
    inv = s1.ask_inventry()
    s1.select_inventry(result, inv)
    ty = s1.ask_inventry()
    rt = s1.ask_quntity()
    df = s1.final(result, ty, rt, inv)
    s1.dump(df)
