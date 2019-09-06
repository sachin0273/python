from OOPS.deck_of_cards import Deck_Of_Card


class Queue_card:
    def sort(self):
        member = int(input("please enter number of members"))
        result = Deck_Of_Card(member).Distribute_Card()
        return result[0]


if __name__ == '__main__':
    result = Queue_card().sort()
    result.sort()
    print(result)
