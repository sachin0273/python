"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we shuffle the deck of cards and distribute card to user entered number of times
        then sort the cards by rank and maintain in queue implemented by linked list
author:  Sachin Shrikant Jadhav
since :  7-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
from OOPS.deck_of_cards import Deck_Of_Card
from data_structure.my_linked_list import Linked_List

linked = Linked_List()
""" here we creating object of linked list class"""


class Queue_Card:
    def __init__(self, member):
        """

        :param member:here we initialize the member attribute

        """
        self.member = member

    def Cards(self):
        """

        :return: here we importing Distribute_Card() method from Deck_Of_Card class and return the,
                cards for each player in 2d array
        """
        cards_result = Deck_Of_Card(self.member).Distribute_Card()  # here we getting cards of each player
        return cards_result

    def Sort(self):
        """

        :return:this method is used for sort the all cards ib 2d array and return the sorted array

        """
        result = self.Cards()
        for row in range(self.member):
            sort_player = result[row]
            sort_player.sort()
            result[row] = sort_player
        return result

    def Queue(self):
        """

        :return:in this method we take sorted array and maintain the player cards in queue

        """
        players = self.Sort()
        for row in range(self.member):
            linked.Add_To_Beginning(players[row])  # this method called from Linked List class

    def Display(self):
        """

        :return: here we display the queue

        """
        player = 1
        while linked.head is not None:
            players = linked.Delete_To_Last_Save()  # this method called from Linked List class
            print()
            print("player :", player)
            print(players)
            player += 1


if __name__ == '__main__':
    while True:
        try:
            member = int(input("please enter number of member"))  # here we taking members from user
            if 0 < member < 6:
                s1 = Queue_Card(member)  # here we creating object of Queue card class
                s1.Queue()
                s1.Display()
                break
            else:
                print("please enter members less than 6")
        except ValueError:
            print("please enter valid input")
