from Utility.utility import Qudratic


def test_check_root():
    """

    :return: in this test case we are checking roots of given equation

    """
    a, b, c = 2, 9, 0
    result = Qudratic(a, b, c)  # here we are calling function from Utility
    assert result == (-6.75, -11.25)
