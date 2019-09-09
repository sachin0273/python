"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this module we created class Address book for taking user input object
author:  Sachin Shrikant Jadhav
since :  7-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""


class Address_book:
    """
    here we creating Address book class in this class we taking addresbook details
    """

    def __init__(self, first_name, last_name, address, city, state, zip,phone_number):  # here we initializing attributes
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number

    def adress_obj(self, object):  # here we catch the all user input objects
        return object.__dict__


if __name__ == '__main__':
    Address_book()
