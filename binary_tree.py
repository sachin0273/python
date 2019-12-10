"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

purpose: in this program we find the number of possible binary tree of given nodes
author:  Sachin Shrikant Jadhav
since :  29-08-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

fact = 1
fact2 = 1
fact3 = 1


def Factorial():
    """
    :param:nodes:here we take number of nodes from user
    :return: in this function we print the number of possible tress of given nodes

    """
    while True:
        try:
            global fact, fact2, fact3
            nodes = int(input("please enter number of nodes"))
            if 0 < nodes < 101:
                node = nodes * 2
                if node > 0:
                    for first_fact in range(1, node + 1):
                        fact = fact * first_fact
                if node > 0:
                    for second_fact in range(1, nodes + 1 + 1):
                        fact2 = fact2 * second_fact
                if node > 0:
                    for third_fact in range(1, nodes + 1):
                        fact3 = fact3 * third_fact
                possible_nodes = fact // (fact2 * fact3)
                return possible_nodes
            else:
                print("please enter number between 1 to 100")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    result = Factorial()
    print("number of possible trees are ------>", result)
