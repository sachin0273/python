import json
import os.path
import re
from Utility.utility import load

state_city = {"maharashtra": ["pune", "nagpur", "solapur", "kolhapur", "sangli"],
              "goa": ['ponda', 'valpoi', 'panaji'], "karnataka": ['bangalore', 'mysore', 'belgaum'],
              "punjab": ['amritsar', 'mohali', 'moga'],
              "gujarat": ['surat', 'vadodara', "jamnagar"]}


class Information:

    def New_File(self):
        while True:
            try:
                file_name = input("please enter file name")
                new_file_name = file_name + ".json"
                with open(new_file_name, "x") as f:
                    return new_file_name
            except Exception:
                print("file already exist")

    def Write_File(self, file_name, user_information):
        with open(file_name, "a")as f:
            json.dump(user_information, f, indent=2, sort_keys=True)

    def Open_File(self):
        while True:
            file_name = input("please enter file_name")
            new_file_name = file_name + ".json"
            if os.path.exists(new_file_name):
                with open(new_file_name) as json_file:
                    data = json.load(json_file)
                    return data, new_file_name
            else:
                print("please enter valid input")

    def First_Name(self):
        while True:
            try:
                first_name = input("please enter your name")
                if first_name.isalpha() and len(first_name) < 9:
                    return first_name
                else:
                    print("please enter valid name in char and length must be less than 9")
            except ValueError:
                print("please enter valid input")

    def Last_Name(self):
        while True:
            try:
                last_name = input("please enter your last name")
                if last_name.isalpha() and len(last_name) < 7:
                    return last_name
                else:
                    print("please enter valid name in char and length must be less than 7")
            except ValueError:
                print("please enter valid input")

    def Address(self):
        while True:
            try:
                adress = input("please enter your address")
                if re.match("^[0-9]+,+\w+,+\w", adress):
                    return adress
                else:
                    print("please enter valid address in (home_number,street_name,city)")
            except ValueError:
                print("please enter valid input")

    def State(self):
        for state in state_city:
            print(state, end=" ")
        print()
        while True:
            try:
                state = input("please enter your State: ")

                if state in state_city:
                    return state
                else:
                    print("please enter state from above list")
            except ValueError:
                print("please enter valid input")

    def City(self, state):
        print("your city's according state--->", state_city[state])
        while True:
            try:
                city = input("please enter your city: ")
                if city in state_city[state]:
                    return city
                else:
                    print("please enter city from above list")
            except ValueError:
                print("please enter valid input")

    def Zip_Code(self):
        while True:
            try:
                zip = int(input("please enter your zip_code"))
                if 0 < zip and re.match("^[416]", str(zip)) and len(str(zip)) == 6:
                    return zip
                else:
                    print("please enter valid zip like 416XXX")
            except ValueError:
                print("please enter valid input")

    def Phone_Number(self):
        # 1) Begins with 0 or 91
        # 2) Then contains 7 or 8 or 9.
        # 3) Then contains 9 digits
        while True:
            try:
                mobile = int(input("please enter mobile number"))
                Pattern = re.compile("^91?[7-9]")
                if Pattern.match(str(mobile)) and len(str(mobile)) == 12:
                    return mobile
                else:
                    print("please enter valid mobile number in 91XXXXXXXXXX format")
            except ValueError:
                print("please enter valid input")

    def Last(self, adresses):
        last_name = set()
        for i in range(len(adresses["address_book"])):
            last_name.add(adresses["address_book"][i]["last_name"])
        last = list(last_name)
        last.sort()
        return last

    def Zip(self, adresses):
        zip_code = set()
        for i in range(len(adresses["address_book"])):
            zip_code.add(adresses["address_book"][i]["zip"])
        zip_codes = list(zip_code)
        zip_codes.sort()
        return zip_codes

    def Sort_Name(self, adresses):
        last_name = self.Last(adresses)
        names = []
        for j in last_name:
            for i in range(len(adresses["address_book"])):
                if j == adresses["address_book"][i]["last_name"]:
                    names.append(adresses["address_book"][i])
        return names

    def Sort_Zip(self, adresses):
        zip_code = self.Zip(adresses)
        zips = []
        for j in zip_code:
            for i in range(len(adresses["address_book"])):
                if j == adresses["address_book"][i]["zip"]:
                    zips.append(adresses["address_book"][i])
        return zips

    def Remove(self, adresses):
        key = input("please enter the name to delete the adress in adress book")
        for i in range(len(adresses["address_book"]) - 1):
            if key == adresses["address_book"][i]["first_name"]:
                del adresses["address_book"][i]
        return adresses

    def Display(self, information):
        for data in information:
            print("first_name: ", data["first_name"], "\n", "last_name: ", data["last_name"])
            print("Address: ", data["address"], "\n", "City: ", data["city"], "\n", "state: ", data["state"])
            print("Zip_code: ", data["zip"], "\n", "phone_number: ", data["phone_number"])
            print()


if __name__ == '__main__':
    fg = Information().Open_File()
