from Utility.utility import Triplets


def test_check_triplets():
    """

    :return: in this test case we are checking adittion of any three element in the array is equal to zero

    """
    array = [0, 1, -1, 9, 6, 8, 5]
    n = len(array)
    result = Triplets(array, n)  # here we are calling function from Utility
    assert result == (0, 1, -1)
