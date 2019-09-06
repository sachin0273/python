from Utility.utility import Gambeler


def test_check_gambeler_output(trails=100):
    """

    :param trails: here we provide number of games play
    :return: this test case used for checking wins of given trails
    """
    result = Gambeler(trails)  # here we calling function from Utility
    assert result < 40
