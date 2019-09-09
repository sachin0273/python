"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we shuffle the deck of cards and distribute card to user entered number of times
author:  Sachin Shrikant Jadhav
since :  7-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
import random


class Deck_Of_Card:
    """
    here we creating class
    """

    def __init__(self, members, cards=None):
        """

        :param members: initializing attribute members
        :param cards: initializing attribute cards

        """
        self.cards = {}
        self.members = members
        self.cards = cards

    def Suits_Shuffle(self):
        """

        :return: this method return the shuffled suits of card

        """
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        random.shuffle(suits)
        return suits

    def Rank_Shuffle(self):
        """

        :return: this method return the shuffled rank of card

        """
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        random.shuffle(rank)
        return rank

    def Distribute_Card(self):
        """

        :return:in this method we distribute the cards user entered number of times

        """
        array = [["" for row in range(9)] for column in range(self.members)]  # here we creating 2d array
        length = self.members * 9
        self.cards = set()
        self.cards.clear()
        while len(self.cards) != length:
            suits = self.Suits_Shuffle()  # here we called suits shuffle method from same class
            ranks = self.Rank_Shuffle()  # here we called Rank shuffle method from same class
            suit = random.choice(suits)
            rank = random.choice(ranks)
            a = (rank, suit)
            self.cards.add(a)
        my_cards = list(self.cards)
        index_y = 0
        index_j = 9
        for member in range(self.members):
            array[member] = my_cards[index_y:index_j]
            index_y = index_j
            index_j += 9
        return array

    def Array(self):
        """

        :return:here we printing cards from array

        """
        result = self.Distribute_Card()
        for player in range(self.members):
            print("player: ", player + 1)
            print(result[player])


if __name__ == '__main__':
    while True:
        try:
            members = int(input("please enter members"))  # here we taking number of players
            if 0 < members < 6:
                card = Deck_Of_Card(members)  # here we creating object of class
                card.Array()
                break
            else:
                print("please enter members less than 6")
        except ValueError:
            print("please enter valid input")
