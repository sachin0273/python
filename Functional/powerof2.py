"""
Purpose:in this program we prints the power table of 2
author : Sachin Shrikant Jadhav
version:3.7
since  : 21-08-2019

"""


def Power_of_two():
    while True:
        try:
            power = int(input("please enter your Number"))
            if 0 <= power < 31:
                for i in range(power):
                    power_table = 2 ** i
                    print(power_table)
                break
            else:
                print("please enter valid number under 31")
        except ValueError:
            print("invalid input")


if __name__ == '__main__':
    Power_of_two()
