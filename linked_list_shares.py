from data_structure.my_linked_list import Linked_List
from Utility.utility import load

linked = Linked_List()


class Shares_Linked_list:

    def Load_File(self):
        shares = load("stock_inventry.json")
        return shares

    def Company_Shares(self, shares):
        for company_share in shares["Stocks"]:
            linked.Add_To_Beginning(company_share["number_of shares"])
        linked.Display()


if __name__ == '__main__':
    in_linked_list = Shares_Linked_list()
    result = in_linked_list.Load_File()
    in_linked_list.Company_Shares(result)
