"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we take name full name mobile number and replace in message,
        and print the replaced string massage
author:  Sachin Shrikant Jadhav
since :  4-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""

from datetime import date
import re


class Regular_Expression:
    """here we created class"""

    def Today_Date(self):
        """
        :return: in this function we importing date and return
        """
        today = date.today()
        today_date = today.strftime("%d/%m/%y")  # here we converted date to appropriate format
        return today_date

    def Valid(self):
        """
        :param:mobile:here we take user input mobile number
        :return: in this function we validate mobile number then return
        """
        # 1) Begins with 0 or 91
        # 2) Then contains 7 or 8 or 9.
        # 3) Then contains 9 digits
        while True:
            try:
                mobile = int(input("please enter mobile number"))
                Pattern = re.compile("^91?[7-9]")  # this is mobile validation regex pattern
                if Pattern.match(str(mobile)) and len(str(mobile)) == 12:
                    return mobile
                else:
                    print("please enter valid mobile number in 91XXXXXXXXXX format")
            except ValueError:
                print("please enter valid input")

    def Full_Name(self):
        """
        :param:full_name:here we take full name from user
        :return: in this function validates full name then return the full name
        """
        name = self.Name()
        while True:
            try:
                length_name = len(name)
                full_name = input("please enter your fullname")
                first_name = full_name[:length_name]
                if re.match('^[a-zA-Z]{2,10}\s[a-zA-Z]{2,10}\s[a-zA-Z]{2,10}$', full_name) and name == first_name:
                    # here is full name validation pattern
                    return full_name, name
                else:
                    print("please enter valid full_name xxxxxxxxx xxxxxxxxx xxxxxxxx format and first name should same")
            except ValueError:
                print("please enter valid name")

    def Name(self):
        """
        :param:name:here we take name input from user
        :return: this function validate name then return
        """
        while True:
            try:
                name = input("please enter your name")
                if name.isalpha() and len(name) < 9:  # validation pattern of name
                    return name
                else:
                    print("please enter valid name length must be less than 9")
            except ValueError:
                print("please enter valid name")

    def Expression(self):
        """
        :param:message:in this parameter message is saved
        :return:in this function takes all input from user and replace with message then print the message

        """
        message = """Hello <<name>>,We have your full name as <<full name>> in our system. your contact number is
        91­xxxxxxxxxx.Please,let us know in case of any clarification Thank you BridgeLabz xx/xx/xxxx. """
        full_name = self.Full_Name()
        mobile_number = self.Valid()
        date = self.Today_Date()
        line = re.sub("<<\w+>>", full_name[1], message)  # name replace regex pattern
        line2 = re.sub("[91]+.+xxxxxxxxxx", str(mobile_number), line)  # mobile number replace regex pattern
        line3 = re.sub("<<\w+\s\w+>>", full_name[0], line2)  # full name replace regex pattern
        send_message = re.sub("xx.xx.xxxx", date, line3)  # here we import date
        print(send_message)


if __name__ == '__main__':
    Regular_Expression().Expression()
