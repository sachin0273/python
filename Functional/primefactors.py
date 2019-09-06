"""

Purpose:in this program we prints the prime factors of given number
author : Sachin Shrikant Jadhav
version:3.7
since  : 21-08-2019


"""


def Prime_Factors():
    while True:
        try:
            number = int(input("please enter your number =  "))
            if 0 < number < 1001:
                for prime_factor in range(2, number + 1 // 2):
                    while number % prime_factor == 0:
                        print(prime_factor, end=" ")
                        number = number // prime_factor
                break
            else:
                print("please enter number between 1 to 1000")
        except ValueError:
            print(" please enter valid input ")


if __name__ == '__main__':
    Prime_Factors()
