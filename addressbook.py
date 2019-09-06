import json


class adressbook:
    def __init__(self, first_name, last_name, adress, city, state, zip, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.adress = adress
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number

    def load(self):
        with open("adressbook.json", 'r') as outfile:
            data = json.load(outfile)
        return data

    def adress_obj(self, obj):
        return obj.__dict__

    def add(self):
        pass

    def last_name(self):
        last_name = []
        data = self.load()
        for i in range(len(data["address_book"])):
            last_name.append(data["address_book"][i]["last_name"])
        last_name.sort()
        return last_name

    def zip(self):
        zip_code = []
        data = self.load()
        for i in range(len(data["address_book"])):
            zip_code.append(data["address_book"][i]["zip"])
        zip_code.sort()
        return zip_code

    def sort_name(self):
        data = self.load()
        last_name = self.last_name()

        for j in last_name:
            for i in range(len(data["address_book"])):
                if j == data["address_book"][i]["last_name"]:
                    print(data["address_book"][i])
                    print()

    def sort_zip(self):
        data = self.load()
        zip_code = self.zip()
        for j in zip_code:
            for i in range(len(data["address_book"])):
                if j == data["address_book"][i]["zip"]:
                    print(data["address_book"][i])
                    print()

    def remove(self):
        data = self.load()
        key = input("please enter the name to delete the adress in adress book")
        for i in data:
            if data[i]["name"] == key:
                del data[i]

    def printing_maling_format(self):
        pass


if __name__ == '__main__':
    adressbook()
