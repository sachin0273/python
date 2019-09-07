from OOPS.deck_of_cards import Deck_Of_Card
from data_structure.my_linked_list import Linked_List

linked = Linked_List()


class Queue_Card:
    def __init__(self, member):
        self.member = member

    def Cards(self):
        cards_result = Deck_Of_Card(self.member).Distribute_Card()
        return cards_result

    def Sort(self):
        result = self.Cards()
        for row in range(self.member):
            sort_player = result[row]
            sort_player.sort()
            result[row] = sort_player
        return result

    def Queue(self):
        players = self.Sort()
        for row in range(self.member):
            linked.Add_To_Beginning(players[row])

    def Display(self):
        player = 1
        while linked.head is not None:
            players = linked.Delete_To_Last_Save()
            print()
            print("player :", player)
            print(players)
            player += 1


if __name__ == '__main__':
    while True:
        try:
            member = int(input("please enter number of member"))
            if 0 < member < 6:
                s1 = Queue_Card(member)
                s1.Queue()
                s1.Display()
            else:
                print("please enter members less than 6")
        except ValueError:
            print("please enter valid input")
