"""

Purpose:in this we Write a Program to play a Cross Game or Tic­Tac­Toe Game. Player 1 is
        the Computer and the Player 2 is the user.finally according to board print the winner
author : sachin shrikant jadhav
version:3.7
since  : 22-08-2019

"""

import random

flag = 0

""" here we create game board"""
board = [" " for row in range(9)]
for i in range(9):
    board[i] = str(i)


def show_board():
    """

    :return: this function used for printing a game board

    """
    print("""------------
    |{}|{}|{}|
    |{}|{}|{}|
    |{}|{}|{}|
    ----------
    """.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7],
               board[8]))


def user_move():
    """
    :purpose: in this function we give input from user called user move
    :return: this function give appropriate position of user move

    """
    try:
        move = int(input("please enter your position (0 to 8)"))
        while move > 8:
            move = int(input("please enter your position (0 to 8)"))

        while board[move] == "X" or board[move] == "O":
            move = int(input("space occupied please enter another position"))
        if move < 9:
            board[move] = "X"
        else:
            return print("enter valid position")

    except Exception as e:
        print(e)


def comp_move():
    """
    :purpose: in this function we give input form random number called computer move
    :return: this function give appropriate position of computer move

    """
    move = random.randint(0, 8)

    while board[move] == "X" or board[move] == "O":
        move = random.randint(0, 8)

    board[move] = "O"


def winner_comp():
    """

    :return: this function gives true if user win

    """
    global j
    j = 0
    winner = ''
    for i in range(3, 10, 3):
        for j in range(j+1, i):
            winner = winner + board[j]
            if winner == "XXX":
                return True
    for i in range(0, 9, 4):
        winner = winner + board[i]
    if winner == "XXX":
        return True
    for i in range(2, 7, 2):
        winner = winner + board[i]
    if winner == "XXX":
        return True


def driver():
    """

    :return: this is driver function of tic tac toe game

    """
    global flag
    for i in range(4):
        user_move()
        comp_move()
        show_board()
        if winner_comp():
            print("sorry you lose youre game try again")
            flag = 1
            break

    if flag == 0:
        user_move()
        show_board()
        if winner_comp():
            print("sorry you lose yours game try again")
        else:
            print("game is draw try again")


if __name__ == '__main__':
    show_board()
    driver()
