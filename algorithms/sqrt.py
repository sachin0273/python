"""
Purpose:in this program we print the square root of given number using Newton's method
author : sachin shrikant jadhav
version:3.7
since  : 24-08-2019
"""


def Square_Root():
    """
    :param:number:here we taking input for computing newtons square root
    :return: this function provide output square root of number using newtons method
    """
    while True:
        try:
            epsilon = 1e-15
            number = int(input("please enter number"))
            if 0 < number < 1001:
                t = number
                while abs(t - number / t) > epsilon * t:
                    t = (number / t + t) / 2.0
                print(t)
                break
            else:
                print("please enter valid number between 1 to 1000")
        except ValueError:
            print("please enter valid input ")


if __name__ == '__main__':
    Square_Root()
