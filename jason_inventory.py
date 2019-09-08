import json



class Inventory:
    dat = 0
    with open('inventry.json', 'r') as outfile:
        data = json.load(outfile)
    for p in data:
        print("{:>7}".format(p), " ""quantity", " ""price_per_kg")
        for i in range(len(data[p])):
            for t in data[p][i].values():
                print("{:>7}".format(t), end=" ")
            print()
        print()
