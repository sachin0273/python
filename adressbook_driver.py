"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we created addresbook for user input addresses 
author:  Sachin Shrikant Jadhav
since :  7-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
from OOPS.addressbook import Address_book
from OOPS.util import Information
import json

book = Information()  # here we creating object of Imported Information class


class Address_Driver(Address_book):  # Address_book is base class and Address_Driver is child class
    def __init__(self, first_name, last_name, address, city, state, zip, phone_number):  # here we use inheritance
        super().__init__(first_name, last_name, address, city, state, zip, phone_number)


if __name__ == '__main__':
    """

    :return: in this  is actual address book here we perform operation like,
                    adding,displaying,sorting,adding user data and remove
    """
    new = {"address_book": []}
    while True:
        try:
            print("please enter your choice: ")
            choice = int(input("1.create_new_address_book\n2.open_adress_book\n3.Exit\n"))
            if choice == 1:
                file = book.New_File()  # here we creating new file
                while True:
                    try:
                        operation = int(input("1.add\n2.Exit"))
                        if operation == 1:
                            first_name = book.First_Name()
                            last_name = book.Last_Name()
                            address = book.Address()
                            state = book.State()
                            city = book.City(state)
                            zip_code = book.Zip_Code()
                            number = book.Phone_Number()
                            slot = Address_Driver(first_name, last_name, address, city, state, zip_code, number)
                            """here we creating object of imported Address book class"""

                            data = json.dumps(slot, default=slot.adress_obj)
                            dump_data = json.loads(data)
                            new["address_book"].append(dump_data)
                            print()
                            print("added successfully")
                        elif operation == 2:
                            with open(file, "w")as f:
                                json.dump(new, f, indent=2)  # here we writing addresses into file
                            break
                        else:
                            print("please enter valid choice")
                    except ValueError:
                        print("please enter valid input")

            elif choice == 2:
                adresess = book.Open_File()  # here we opening existing file
                while True:
                    try:
                        user_input = int(input("1.add\n2.display\n3.sort_by_last_name\n4.sort_by_zip\n5"
                                               ".Remove_Address\n6 "
                                               ".Exit"))
                        if user_input == 1:
                            first_name = book.First_Name()
                            last_name = book.Last_Name()
                            address = book.Address()
                            state = book.State()
                            city = book.City(state)
                            zip_code = book.Zip_Code()
                            number = book.Phone_Number()
                            new = Address_book(first_name, last_name, address, city, state, zip_code, number)
                            """here we creating object of imported Address book class"""

                            data = json.dumps(new, default=new.adress_obj)
                            dump_new_data = json.loads(data)
                            adresess[0]["address_book"].append(dump_new_data)
                            with open(adresess[1], "w")as f:
                                json.dump(adresess[0], f, indent=2)  # here we writing addresses into file
                            print()
                            print("added successfully")
                        elif user_input == 2:
                            book.Display(adresess[0]["address_book"])  # here displaying addresses

                        elif user_input == 3:
                            result_name = book.Sort_Name(adresess[0])  # here sorting addresses by last name
                            book.Display(result_name)

                        elif user_input == 4:
                            result_zip = book.Sort_Zip(adresess[0])  # here sorting addresses by zip code
                            book.Display(result_zip)
                        elif user_input == 5:
                            result = book.Remove(adresess[0])  # here removing addresses by name
                            with open(adresess[1], "w")as f:
                                json.dump(result, f, indent=2,
                                          sort_keys=False)  # here writing addresses after removing
                            print("removed successfully")
                        elif user_input == 6:
                            break
                        else:
                            print("please enter valid choice")
                    except ValueError:
                        print("please enter valid input")
            elif choice == 3:
                break
            else:
                print("please enter valid choice")
        except ValueError:
            print("please enter valid input")
