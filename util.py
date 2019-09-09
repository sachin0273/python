"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this we creating utility for addresbook.py module so most of the code can be reused
author:  Sachin Shrikant Jadhav
since :  7-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
import json
import os.path
import re

state_city = {"maharashtra": ["pune", "nagpur", "solapur", "kolhapur", "sangli"],
              "goa": ['ponda', 'valpoi', 'panaji'], "karnataka": ['bangalore', 'mysore', 'belgaum'],
              "punjab": ['amritsar', 'mohali', 'moga'],
              "gujarat": ['surat', 'vadodara', "jamnagar"]}


class Information:
    """here we creating Information class"""

    def New_File(self):
        """

        :return: this method is used for creating new file if file exist throw exception
        """
        while True:
            try:
                file_name = input("please enter file name")
                if 3 < len(file_name) < 20 and file_name.isalpha():
                    new_file_name = file_name + ".json"
                    with open(new_file_name, "x") as f:
                        return new_file_name
                else:
                    print("length of file name should be greater then 3 and less than 20")
            except Exception:
                print("file already exist")

    def Write_File(self, file_name, user_information):
        """

        :param file_name: here we pass file name for writing
        :param user_information: here we pass data for writing
        :return: this method write the data given file
        """
        with open(file_name, "a")as f:
            json.dump(user_information, f, indent=2, sort_keys=True)

    def Open_File(self):
        """

        :return: this method is used for open a exist file

        """
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
        """

        :return:this method return the user input first name

        """
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
        """

        :return: this method return the user input last name

        """
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
        """

        :return: this method return the user input Address after validation

        """
        while True:
            try:
                adress = input("please enter your address")
                if re.match('^[1-9]{4}\s[a-zA-Z]{2,20}\s[a-zA-Z]{2,15}$', adress):  # pattern for address validation
                    return adress
                else:
                    print("please enter valid address in (home_number(e.g-1987) street_name city) format")
            except ValueError:
                print("please enter valid input")

    def State(self):
        """

        :return:this method return user input State name after validation

        """
        for state in state_city:  # printing available states
            print(state, end=" ")
        print()
        while True:
            try:
                state = input("please enter your State: ")

                if state in state_city:  # validation of state
                    return state
                else:
                    print("please enter state from above list")
            except ValueError:
                print("please enter valid input")

    def City(self, state):
        """

        :param state: here we pass state name for select appropriate city
        :return:this method return city after validation

        """
        print("your city's according state--->", state_city[state])  # here we printing city according state
        while True:
            try:
                city = input("please enter your city: ")
                if city in state_city[state]:  # here we checking or validate city
                    return city
                else:
                    print("please enter city from above list")
            except ValueError:
                print("please enter valid input")

    def Zip_Code(self):
        """

        :return: this function return the user input zip_code after validation\

        """
        while True:
            try:
                zip = int(input("please enter your zip_code"))
                if 0 < zip and re.match("^[416]", str(zip)) and len(str(zip)) == 6:  # here pattern for validation
                    return zip
                else:
                    print("please enter valid zip like 416XXX")
            except ValueError:
                print("please enter valid input")

    def Phone_Number(self):
        """

        :return:in this method we return the user input phone number after validation

        """
        # 1) Begins with 0 or 91
        # 2) Then contains 7 or 8 or 9.
        # 3) Then contains 9 digits
        while True:
            try:
                mobile = int(input("please enter mobile number"))
                Pattern = re.compile("^91?[7-9]")  # here pattern for mobile validation
                if Pattern.match(str(mobile)) and len(str(mobile)) == 12:
                    return mobile
                else:
                    print("please enter valid mobile number in 91,7-9,XXXXXXXX format")
            except ValueError:
                print("please enter valid input")

    def Last(self, adresses):
        """

        :param adresses: here we taking all adresses from addresbook json file
        :return: this method return last names in addresbook
        """
        last_name = set()
        for index in range(len(adresses["address_book"])):
            last_name.add(adresses["address_book"][index]["last_name"])
        last = list(last_name)
        last.sort()
        return last

    def Zip(self, adresses):
        """

        :param adresses: here we taking all adresses from addresbook json file
        :return: this method return zip codes in addresbook

        """
        zip_code = set()
        for index in range(len(adresses["address_book"])):
            zip_code.add(adresses["address_book"][index]["zip"])
        zip_codes = list(zip_code)
        zip_codes.sort()
        return zip_codes

    def Sort_Name(self, adresses):
        """

        :param adresses: here we taking all adresses from addresbook json file
        :return: this function return the sorted by last name addresbook

        """
        last_name = self.Last(adresses)
        names = []
        for name in last_name:
            for index in range(len(adresses["address_book"])):
                if name == adresses["address_book"][index]["last_name"]:
                    names.append(adresses["address_book"][index])
        return names

    def Sort_Zip(self, adresses):
        """

        :param adresses: here we taking all adresses from addresbook json file
        :return: this function return the sorted by zip_code addresbook

        """
        zip_code = self.Zip(adresses)
        zips = []
        for code in zip_code:
            for index in range(len(adresses["address_book"])):
                if code == adresses["address_book"][index]["zip"]:
                    zips.append(adresses["address_book"][index])
        return zips

    def Remove(self, adresses):
        """

        :param adresses: here we taking all adresses from addresbook json file
        :return: this function used for delete address according to user input name
        """
        while True:
            key = input("please enter the name to delete the adress in adress book")
            for i in range(len(adresses["address_book"]) - 1):
                if key == adresses["address_book"][i]["first_name"] and key.isalpha():
                    del adresses["address_book"][i]
                    return adresses

    def Display(self, information):
        """

        :param information: here we taking all adresses from addresbook json file
        :return:here we displaying the addresbook in mailing format

        """
        for data in information:
            print("first_name: ", data["first_name"], "\n", "last_name: ", data["last_name"])
            print("Address: ", data["address"], "\n", "City: ", data["city"], "\n", "state: ", data["state"])
            print("Zip_code: ", data["zip"], "\n", "phone_number: ", data["phone_number"])
            print()


if __name__ == '__main__':
    fg = Information().Phone_Number()
