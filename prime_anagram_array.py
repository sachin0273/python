"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
purpose: in this program we print the anagram number or not anagram prime number between 1 to 1000 in 2d array
author:  Sachin Shrikant Jadhav
since :  28-08-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

from Utility.utility import Prime_Number

array = [["" for column in range(107)] for row in range(2)]  # here we creating 2d array

result = Prime_Number(1000)  # here we calling function from utility for prime numbers


def Prime_Array():
    """

    :return:this function returns anagram in first row and not anagram in second row

    """
    try:
        r_index, t_index = 0, 0
        for prime_numbers in range(len(result)):  # here we iterating prime numbers

            flag = 1
            for prime_number in range(prime_numbers + 1, len(result)):
                if sorted(str(result[prime_numbers])) == sorted(str(result[prime_number])):
                    array[0][r_index] = result[prime_number]  # here we appending anagrams in row 1
                    r_index += 1
                    flag = 0
            if flag == 1:
                array[1][t_index] = result[prime_numbers]  # here we appending not anagrams in row 2
                t_index += 1
        return array
    except Exception as e:
        print(e)


if __name__ == '__main__':
    result = Prime_Array()
    for row in range(2):  # here we printing 2d array
        for column in range(107):
            print(result[row][column], end=" ")
        print()
