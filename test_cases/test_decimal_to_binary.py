from Utility.utility import To_Binary


def test_binary():
    """

    :return: in this test case we check binary of given input

    """
    decimal_number = 100
    result = To_Binary(decimal_number)  # here we calling function from Utility
    assert result == [1, 1, 0, 0, 1, 0, 0]
    assert type(decimal_number) == int
