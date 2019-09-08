from OOPS.addressbook import Address_book
from OOPS.util import Information
import json

book = Information()


def Driver():
    new = {"address_book": []}
    while True:
        try:
            print("please enter your choice: ")
            choice = int(input("1.create_new_address_book\n2.open_adress_book\n3.Exit\n"))
            if choice == 1:
                file = book.New_File()
                while True:
                    operation = int(input("1.add\n2.Exit"))
                    if operation == 1:
                        first_name = book.First_Name()
                        last_name = book.Last_Name()
                        address = book.Address()
                        state = book.State()
                        city = book.City(state)
                        zip_code = book.Zip_Code()
                        number = book.Phone_Number()
                        slot = Address_book(first_name, last_name, address, city, state, zip_code, number)

                        data = json.dumps(slot, default=slot.adress_obj)
                        print(data)
                        new["address_book"].append(data)
                        data2 = json.dumps(new)
                        print(data2)
                    elif operation == 2:
                        # with open(file, "w")as f:
                        #     json.dump(new, f, indent=4, sort_keys=False)
                        break
                    else:
                        print("please enter valid choice")

            elif choice == 2:
                adresess = book.Open_File()
                user_input = int(
                    input("1.add\n2.display\n3.sort_by_last_name\n4.sort_by_zip\n5.Remove_Address\n6.Exit"))
                if user_input == 1:
                    first_name = book.First_Name()
                    last_name = book.Last_Name()
                    address = book.Address()
                    state = book.State()
                    city = book.City(state)
                    zip_code = book.Zip_Code()
                    number = book.Phone_Number()
                    new = Address_book(first_name, last_name, address, city, state, zip_code, number)
                    data = json.dumps(new, default=new.adress_obj)
                    adresess[0]["address_book"].append(data)
                    with open(adresess[1], "w")as f:
                        json.dump(adresess[0], f, indent=2, default=new.adress_obj, sort_keys=False)

                elif user_input == 2:
                    book.Display(adresess[0]["address_book"])

                elif user_input == 3:
                    result_name = book.Sort_Name(adresess[0])
                    book.Display(result_name)

                elif user_input == 4:
                    result_zip = book.Sort_Zip(adresess[0])
                    book.Display(result_zip)
                elif user_input == 5:
                    result = book.Remove(adresess[0])
                    with open(adresess[1], "w")as f:
                        json.dump(result, f, indent=2, sort_keys=False)
                elif user_input == 6:
                    return

            elif choice == 3:
                return

            else:
                print("please enter valid choice")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Driver()
