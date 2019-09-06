"""
 Purpose:it is Utility Class where logic of all other programs are written .
         This is done so most of the code can be reused
 author:  Sachin Shrikant Jadhav
 since :  21-08-2019
 
"""
import random
import math
import json


def User_Name(User_name):
    """
    \
    :param User_name: here we take input from user and replace input string into the template
    :return:           this function give output replaced string template

    """
    if type(User_name) == str and User_name.isalpha():
        template = "Hello <<UserName>> How are you?"
        replaced_template = template.replace("<<UserName>>", User_name, 1)
        return replaced_template
    else:
        return False


def Leap_Or_Not(year):
    """

    :param year: here we pass year for check leap or not
    :return:  this function gives output input year is leap or not

    """
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("leap_year")
        return True
    else:
        print("not leap year")
        return False


def Qudratic(A, B, C):
    """

    :param A: this is A parameter of equation
    :param B: this is C parameter of equation
    :param C: this is C parameter of equation
    :return:   this function give output roots of equation
    """
    delta = B * B - 4 * A * C
    if delta > 0:
        Root1 = -B + math.sqrt(delta) / (2 * A)
        Root2 = -B - math.sqrt(delta) / (2 * A)
        return Root1, Root2
    elif delta == 0:
        root1 = -B / (2 * A)
        root2 = -B / (2 * A)
        print("two equal real root exists")
        return root1, root2


def Triplets(array, n):
    """

    :param array: here we pass the array of number
    :param n: here we pass length of array
    :return: this function give output triplets addition of zero
    """
    for first in range(0, n - 2):
        for second in range(first + 1, n - 1):
            for third in range(second + 1, n):
                if array[first] + array[second] + array[third] == 0:
                    return array[first], array[second], array[third]
    return "no triplets"


def Harmonic_Number(Nth_number):
    """

    :param Nth_number: here we get nth harmonic number
    :return: this function give addition of nth harmonic number
    """
    if type(Nth_number) == int:
        harmonicnumber = 0
        for number_range in range(1, Nth_number):
            harmonicnumber = harmonicnumber + 1 / number_range
        return harmonicnumber
    else:
        return False


def Gambeler(trails, Stake, goal):
    """

    :param trails: here we pass the number of time to play game
    :param Stake: this is starting amount of bet
    :param goal: this is winning number if reach this number will be win
    :return:  this function give output number of wins between number of times you play
    """
    Number_of_bets = 0
    win = 0
    for games in range(trails):
        cash = Stake
        while 0 < cash < goal:
            Number_of_bets += 1
            if random.random() < 0.5:
                cash += 1
            else:
                cash -= 1

            if cash == goal:
                win += 1
    return win


def Flip_Coin(times):
    """

    :param times: here we pass number of times
    :return: this function give output number of heads and tails
    """
    count = 0
    count2 = 0
    for flip in range(times):
        random_number = random.random()
        if random_number < 0.5:
            count += 1  # it is for heads
        else:
            count2 += 1  # it is for tails
    return count, count2


def Line_Distance(X, Y):
    """

    :param X: this is input x parameter of equation
    :param Y: this is input y parameter of equation
    :return: this function give  distance of equation
    """
    Distance = math.sqrt(X ** 2 + Y ** 2)
    return Distance


def Coupn(number_of_coupons):
    """

    :param number_of_coupons: here we pass number of coupons we want
    :return: this function give output N distinct coupn

    """
    if type(number_of_coupons) == int:
        alpha_list = ["a", "b", "c", "d", "e", "f", "A", "o", "Q", "I", "B", "F", "X"]
        Distinct_Coupon = set()
        while len(Distinct_Coupon) < number_of_coupons:
            random1 = random.randint(0, 100)
            random2 = random.choice(alpha_list)
            total_coupn = random2 + str(random1)
            Distinct_Coupon.add(total_coupn)

        return Distinct_Coupon
    else:
        return False


def Prime_Number(prime_range):
    """

    :param prime_range: here we pass range of numbers
    :return: this function gives output number of prime numbers within range
    """
    if type(prime_range) == int:
        prime_list = []
        flag = True
        for prime_number in range(2, prime_range):
            for number in range(2, prime_number):
                if prime_number % number == 0:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                prime_list.append(prime_number)

        return prime_list
    else:
        return False


def Is_Anagram(first_string, second_string):
    """

    :param first_string: here we pass first string for check anagram
    :param second_string: here we pass second string for check anagram
    :return: this function gives output both string anagram or not for each other
    """
    if type(first_string) and type(second_string) == int:
        return False
    else:
        anagram = True
        str1 = ''.join(sorted(first_string))
        str2 = ''.join(sorted(second_string))
        if len(first_string) != len(second_string):
            return not anagram
        elif str1 == str2:
            return anagram
        else:
            return not anagram


def Binary_Search(item_list, item):
    """

    :param item_list: here we pass string list
    :param item: here we pass item for search in string list
    :return:    this function gives output item is present in string list or not

    """
    first = 0
    last = len(item_list) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


def Insertion_Sort(item_list):
    """

    :param item_list: here we pass unsorted list of integers
    :return: this function gives output sorted list
    """
    for index in range(1, len(item_list)):

        current_value = item_list[index]
        position = index

        while position > 0 and item_list[position - 1] > current_value:
            item_list[position] = item_list[position - 1]
            position = position - 1
            item_list[position] = current_value
    return item_list


def Bubble_Sort(item_list):
    """

    :param item_list: here we pass unsorted list of integers or string
    :return: this function give output sorted list of integers or string
    """
    if type(item_list) == list:
        for pass_num in range(len(item_list) - 1, 0, -1):
            for i in range(pass_num):
                if item_list[i] > item_list[i + 1]:
                    temp = item_list[i]
                    item_list[i] = item_list[i + 1]
                    item_list[i + 1] = temp
        return item_list
    else:
        return False


def Guess_Number(number_list):
    """

    :param number_list:here we pass number list
    :return: function returns the guessed number

    """
    global mid
    first = 0
    last = len(number_list) - 1
    print("please think a number between", first, "-", last)
    while first < last:
        mid = (first + last) // 2
        print("number=", mid, )
        true = bool(int(input("if your number greater than above number\n type 1 or if equal and less type 0")))
        if true:
            first = mid + 1
        elif not true:
            last = mid - 1
        else:
            break
    return number_list[mid]


def File_Reader(file_name):
    """

    :param file_name: here we pass path of file
    :return:         this function gives output content in the file
    """
    f = open(file_name, "r")
    if f.mode == "r":
        contents = f.read()
        return contents


def File_Int_Reader(file_name):
    """

    :param file_name: here we pass path of file
    :return: this function reads the integer content in the file

    """
    theFile = open(file_name, "r")
    theInts = []
    for val in theFile.read().split(","):
        theInts.append(int(val))
    theFile.close()
    return theInts


def Vending(input_amount):
    """

    :param input_amount: here we pass the amount for the change
    :return: this function gives change of given amount as minimum notes

    """
    rem = input_amount
    change_list = {}
    while rem != 0:
        input_amount = rem
        note = [1, 2, 5, 10, 50, 100, 500, 1000]
        note_range = len(note)
        for i in range(note_range):
            Note2 = 0
            if rem < note[i]:
                rem = rem % note[i - 1]
                input_amount = input_amount // note[i - 1]
                Note2 += input_amount
                change_list.update({note[i - 1]: Note2})
                break
            elif rem > note[7]:
                rem = rem % note[7]
                input_amount = input_amount // note[7]
                Note2 += input_amount
                change_list.update({note[7]: Note2})
                break

    return change_list


def Day_Of_Week(day, month, year):
    """

    :param day: here we pass day of date
    :param month: here we pass month of date
    :param year: here we pass year of date
    :return:  this function gives day of week according input date
    """
    if type(day and month and year) == int:
        y = year - (14 - month) // 12
        x = y + y // 4 - y // 100 + y // 400
        m = month + 12 * ((14 - month) // 12) - 2
        d = (day + x + 31 * m // 12) % 7
        return d
    else:
        return False


def To_Binary(number):
    """

    :param number: here we pass number to convert into binary
    :return: this function gives output binary of given number


    """
    power = 1
    binary_list = []
    while power <= number // 2:
        power *= 2
    while power > 0:
        if power > number:
            binary_list.append(0)
        else:
            binary_list.append(1)
            number = number - power
        power = power // 2

    return binary_list


def Permutation(string):
    """

    :param string: here we pass the user input string for permutation
    :return: this function gives output number of permutations of given string

    """
    if len(string) == 1:
        return string

    perms = Permutation(string[1:])  # recursion
    char = string[0]
    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
    return result


def File_Writer(file_name, file_data):
    f = open(file_name, "w")
    for word in file_data:
        f.write("{:<6}".format(word))
    f.close()


def load(file_name):
    with open(file_name, 'r') as outfile:
        data = json.load(outfile)
    return data
