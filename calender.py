"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
purpose: in this program we take user input year and month and print calender
author:  Sachin Shrikant Jadhav
since :  27-08-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

from Utility.utility import Day_Of_Week
from Utility.utility import Leap_Or_Not

array = [["" for i in range(7)] for j in range(7)]  # here we creating 2d array


def Two_D_Array_Calender():
    """

    :param:here we get year of calender
    :param:here we get month of calender
    :return: this function print the calender of given input

    """
    while True:
        try:
            year = int(input("enter year"))
            day = 1
            month = int(input("enter month"))
            if 0 < month < 13 and len(str(year)) == 4:
                days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # here is days of given month
                array[0][:] = ["S", "M", "T", "W", "Th", "F", "S"]
                index_row = 1

                if month == 2 and Leap_Or_Not(year) is True:  # here we check given year is leap or not
                    days[month] = 29

                start_day = Day_Of_Week(day, month, year)  # here we finding the day of week using calling function from
                # utility

                for space in range(start_day):  # here we printing space upto staring day
                    array[1][space] = " "
                index_col = start_day

                for days in range(1, days[month] + 1):  # here we adding days into 2d array
                    (array[index_row][index_col]) = days
                    index_col += 1

                    if (days + start_day) % 7 == 0:
                        index_row += 1
                        index_col = 0

                return array
            else:
                print("please enter valid input year and month XXXX/XX")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    result = Two_D_Array_Calender()
    for row in range(7):
        for column in range(7):
            print('{:>2}'.format(result[row][column]), end=" ")  # here we printing calender from 2d array
        print()
