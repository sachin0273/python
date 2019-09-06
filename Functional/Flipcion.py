"""

Purpose:in this program we prints number of heads and tails between coin flipped
author : Sachin Shrikant Jadhav
version:3.7
since  : 21-08-2019

"""
from Utility.utility import Flip_Coin

while True:
    """
    
    :param:times: here we get input for number of times flip a coin
    
    """
    try:
        times = int(input("please enter number of times you flip a coin"))
        if times < 10001:
            result = Flip_Coin(times)  # here we'tuple' object is not callable calling flip_coin function from utility
            print(("head", "tails ="), result)
            break
        else:
            print("please enter number in 1 to 10000 range")
    except ValueError:
        print("please enter valid input")
