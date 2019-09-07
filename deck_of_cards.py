import random


class Deck_Of_Card:
    def __init__(self, members, cards=None):
        self.cards = {}
        self.members = members
        self.cards = cards

    def Suits_Shuffle(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        random.shuffle(suits)
        return suits

    def Rank_Shuffle(self):
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        random.shuffle(rank)
        return rank

    def Distribute_Card(self):
        array = [["" for row in range(self.members)] for column in range(9)]
        length = self.members * 9
        self.cards = set()
        self.cards.clear()
        while len(self.cards) != length:
            suits = self.Suits_Shuffle()
            ranks = self.Rank_Shuffle()
            suit = random.choice(suits)
            rank = random.choice(ranks)
            a = (rank, suit)
            self.cards.add(a)
        my_cards = list(self.cards)
        index_y = 0
        index_j = 9
        for member in range(self.members):
            print("player", member + 1, "cards: ")
            print(my_cards[index_y:index_j])
            array[member] = my_cards[index_y:index_j]
            index_y = index_j
            index_j += 9
        return array


if __name__ == '__main__':
    while True:
        try:
            members = int(input("please enter members"))
            if 0 < members < 6:
                card = Deck_Of_Card(members)
                card.Distribute_Card()
                break
            else:
                print("please enter members less than 6")
        except ValueError:
            print("please enter valid input")
