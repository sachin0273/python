"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
purpose: in this program we print the prime  number between 1 to 1000 in 2d array
author:  Sachin Shrikant Jadhav
since :  28-08-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

from Utility.utility import Prime_Number

_2d_array = [["" for column in range(100)] for row in range(20)]  # here we creating 2d array


def Prime_2d_Array():
    """

    :return: this function return 2d array with prime number

    """
    try:
        low, low1 = 0, 0  # ranges for iteration
        high, high1 = 100, 100
        f_index = 0

        for row in range(0, 20, 2):  # here we updating 2d array with 1 to 1000 number
            for number in range(low, high):
                (_2d_array[row][f_index]) = number + 1
                f_index += 1
            low = high
            high = high + 100
            f_index = 0
        prime_result = Prime_Number(1000)  # here we calling function from utility for prime number between range 1
        # to 1000
        k_index = 1
        h_index = 0

        for prime_number in range(len(prime_result)):  # here we updating 2d array with prime number

            if low1 <= prime_result[prime_number] < high1:
                (_2d_array[k_index][h_index]) = prime_result[prime_number]
                h_index += 1
            else:
                low1 = high1
                high1 = high1 + 100
                k_index += 2
                h_index = 0
        return _2d_array

    except Exception and ValueError as e:
        print(e)


if __name__ == '__main__':
    result = Prime_2d_Array()
    print(result)
    for row in range(20):  # here we printing 2d array
        for column in range(100):
            print(result[row][column], end=" ")
        print()
