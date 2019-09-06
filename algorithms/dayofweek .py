"""

Purpose:in this program we take Date from user and print the day of week
author : sachin shrikant jadhav
version:3.7
since  : 24-08-2019

"""

from Utility.utility import Day_Of_Week


def Day_Of_Week_Driver():
    while True:
        try:
            print("enter date in", "xx/xx/xxxx", "format")
            day, month, year = int(input("day/")), int(input("month/")), int(input("year/"))
            if 0 < day < 31 and 0 < month < 13 and len(str(year)) == 4:
                result = Day_Of_Week(day, month, year)  # here we calling day of week function from Utility
                day_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                            'saturday']  # here days of week
                print("day of week is ---->", day_list[result])
            else:
                print("please enter valid date")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Day_Of_Week_Driver()
