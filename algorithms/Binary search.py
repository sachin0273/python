"""

Purpose:in this program we read the word file and check the user input word is present or not
author : sachin shrikant jadhav
version:3.7
since  : 23-08-2019

"""

from Utility.utility import Binary_Search
from Utility.utility import File_Reader


def Binary_Search_Driver():
    """

    :param:word: here we take word input from user
    :return:in this function we return the word found or not

    """

    try:
        word = File_Reader("new.txt")  # here we calling file reader function from utility
        word_list = word.split(",")
        word_data = sorted(word_list, reverse=False)
        print('listing all the data :', word_data)
        while True:
            word = input("please input a word for searching")
            if word.isalpha() and len(word) < 10:
                result = Binary_Search(word_data, word)  # here we calling binary search function from utility
                if result:
                    print("word found")
                else:
                    print("word not found")
                break
            else:
                print("please enter valid input in char or length less than 10")

    except FileNotFoundError or ValueError:
        print("please enter valid file path")


if __name__ == '__main__':
    Binary_Search_Driver()
