"""



"""
from datetime import date

today = date.today()
dat = today.strftime("%d/%m/%y")
print(dat)

import re


def isValid(s):
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(s)


def regular_expression():
    message = """Hello <<name>>,We have your full name as <<full name>> in our system. your contact number is
    91­xxxxxxxxxx.Please,let us know in case of any clarification Thank you BridgeLabz xx/xx/xxxx. """
    name = input("enter your name")
    full_name = input("enter full name")
    mobile_number = input("enter mobile number ")
    if isValid(mobile_number):
        line = re.sub("<<\w+>>", name, message)
        lin = re.sub("[91]+.+xxxxxxxxxx", mobile_number, line)
        li = re.sub("<<\w+\s\w+>>", full_name, lin)
        l = re.sub("xx.xx.xxxx", dat, li)
    else:
        print("check mobile number")
    print(l)


if __name__ == '__main__':
    regular_expression()
