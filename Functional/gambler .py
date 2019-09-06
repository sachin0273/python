"""

Purpose:in this program we prints the number of win and win or loss percentage of given trails
author : Sachin Shrikant Jadhav
version:3.7
since  : 21-08-2019

"""
from Utility.utility import Gambeler


def Gambler_Driver():
    while True:
        try:
            trails = int(input("please enter your number of trails: "))
            if 0 < trails < 1001:
                Stake = 50
                goal = 300
                win = Gambeler(trails, Stake, goal)  # here we calling function gambler from utility
                win_percent = win / trails * 100
                print("wins = ", win)
                print("youre win percentage is = ", win_percent, "%")
                print("your loss percentage is = ", 100 - win_percent, "%")
                break
            else:
                print("please enter number between 1 to 1000: ")

        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Gambler_Driver()
