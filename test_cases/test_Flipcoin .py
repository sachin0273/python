from Utility.utility import Flip_Coin


def test_flip_output():
    """

    :return: in this test case we check number of heads or tails of given times

    """
    data_to_use = 1000
    result = Flip_Coin(data_to_use)  # here we calling function from Utility
    assert result < (600, 500)
