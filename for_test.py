import re

from OOPS.deck_of_cards import Deck_Of_Card


class Test:
    def Address(self, adress):
        if re.match('^[1-9]{4}\s[a-zA-Z]{2,20}\s[a-zA-Z]{2,15}$', adress):
            return adress
        else:
            return False

    def State(self, state):
        state_city = ["goa", "maharashtra", "punjab", "gujarat"]
        if state in state_city:
            return state
        else:
            return False

    def City(self, city):
        state_city = ["mumbai", "nagpur", "kolhapur"]
        if city in state_city:
            return city
        else:
            return False

    def Zip_Code(self, zip_code):
        if re.match("^[416]", str(zip_code)) and len(str(zip_code)) == 6:
            return zip_code
        else:
            return False

    def Phone_Number(self, number):
        Pattern = re.compile("^91?[7-9]")
        if Pattern.match(str(number)) and len(str(number)) == 12:
            return number
        else:
            return False

    def Full_Name(self, full_name):
        if re.match('^[a-zA-Z]{2,10}\s[a-zA-Z]{2,10}\s[a-zA-Z]{2,10}$', full_name):
            return full_name
        else:
            return False

    def Deck_Of_Card_test(self, member):
        if len(str(member)) < 6 and type(member) == int:
            card = Deck_Of_Card(member).Distribute_Card()
            return len(card)
        if type(member) == str:
            return False
        else:
            return False
