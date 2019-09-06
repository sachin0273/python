from Utility.utility import Guess_Number


def Guess_Number_Driver():
    """

    :return: here we printing guessed number between given number 2^number

    """
    while True:
        try:
            number = int(input("please enter a any number"))
            number_range = 2 ** number
            if 0 < number < 11:
                number_list = []
                for i in range(number_range):
                    number_list.append(i)
                print(number_list)
                guessed_number = Guess_Number(
                    number_list)  # here we calling binary search function for guess number from
                # Utility
                print(guessed_number)
            else:
                print("please enter valid input between 1 to 10")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Guess_Number_Driver()
