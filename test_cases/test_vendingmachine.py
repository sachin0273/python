from Utility.utility import Vending


def test_check_vending():
    """

    :return: in this test case we are checking minimum change of given amount

    """
    change = 40000
    result = Vending(change)  # here we calling function from Utility
    assert result == {1000: 40}
    assert type(change) == int
