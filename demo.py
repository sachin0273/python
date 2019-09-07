fg = {"maharashtra": ["pune", "nagpur", "solapur", "kolhapur", "sangli"],
      "goa": ['ponda', 'valpoi', 'panaji'], "karnataka": ['bangalore', 'mysore', 'belgaum'],
      "punjab": ['amritsar', 'mohali', 'moga'],
      "gujarat": ['surat', 'vadodara', "jamnagar"]}
import json


class adressbook:
    def __init__(self, first_name, last_name, adress, city, state, zip, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.adress = adress
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number

    def adress_obj(self,object):
        return object.__dict__


slot = adressbook("ff", "gg", "gg", "grg", "gg", "ggg", "ggg")
data = json.dumps(slot, default=slot.adress_obj)
print(data)
