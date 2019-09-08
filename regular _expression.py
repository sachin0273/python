"""



"""
from datetime import date
import re


class Regular_Expression:

    def Today_Date(self):
        today = date.today()
        today_date = today.strftime("%d/%m/%y")
        return today_date

    def Valid(self):
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

    def Full_Name(self):
        name = self.Name()
        while True:
            try:
                g = len(name)
                full_name = input("please enter your fullname")
                fg = full_name[:g]
                if re.match('^[a-zA-Z]{2,10}\s[a-zA-Z]{2,10}\s[a-zA-Z]{2,10}$', full_name) and name == fg:
                    return full_name, name
                else:
                    print("please enter valid full_name xxxxxxxxx xxxxxxxxx xxxxxxxx format and first name should same")
            except ValueError:
                print("please enter valid name")

    def Name(self):
        while True:
            try:
                name = input("please enter your name")
                if name.isalpha() and len(name) < 9:
                    return name
                else:
                    print("please enter valid name length must be less than 9")
            except ValueError:
                print("please enter valid name")

    def Expression(self):
        message = """Hello <<name>>,We have your full name as <<full name>> in our system. your contact number is
        91­xxxxxxxxxx.Please,let us know in case of any clarification Thank you BridgeLabz xx/xx/xxxx. """
        full_name = self.Full_Name()
        mobile_number = self.Valid()
        date = self.Today_Date()
        line = re.sub("<<\w+>>", full_name[1], message)
        line2 = re.sub("[91]+.+xxxxxxxxxx", str(mobile_number), line)
        line3 = re.sub("<<\w+\s\w+>>", full_name[0], line2)
        send_message = re.sub("xx.xx.xxxx", date, line3)
        print(send_message)


if __name__ == '__main__':
    Regular_Expression().Expression()
