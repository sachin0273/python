"""

Purpose:in this program we prints the Euclidean distance from the point (x,y) to the origin (0,0)
author : sachin shrikant jadhav
version:3.7
since  : 22-08-2019

"""
from Utility.utility import Line_Distance


def Distance_Driver():
    while True:
        try:
            point_x = int(input("enter a x point"))
            point_y = int(input("enter a y point"))
            if 0 < point_x and point_y < 101:
                result = Line_Distance(point_x, point_y)
                print(result)
                break
            else:
                print("please enter valid numbers between 1 to 100")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Distance_Driver()
