
class Address_book:
    def __init__(self, first_name, last_name, address, city, state, zip, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number

    def adress_obj(self ,object):
        return object.__dict__


if __name__ == '__main__':
    Address_book()
