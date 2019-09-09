"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this program we maintain the stock shares in linked list
author:  Sachin Shrikant Jadhav
since :  7-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""


from data_structure.my_linked_list import Linked_List
from Utility.utility import load

linked = Linked_List()


class Shares_Linked_list:
    """ here we creating the class"""

    def Load_File(self):
        """

        :return: in this method we getting all details of stock inventory
        """
        shares = load("stock_inventry.json")
        return shares

    def Company_Shares(self, shares):
        """

        :param shares: here we taking shares of each Stock from stock inventory json file
        :return:this method maintain the shares in linked list

        """
        for company_share in shares["Stocks"]:
            linked.Add_To_Beginning(company_share["number_of shares"])
        linked.Display()


if __name__ == '__main__':
    in_linked_list = Shares_Linked_list()
    result = in_linked_list.Load_File()
    in_linked_list.Company_Shares(result)
