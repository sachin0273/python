from algorithms.extendedprime import Prime_Palindrome
from Utility.utility import Prime_Number


def test_pelindrom():
    """

    :return: in this test case we are checking palindrome or anagram prime number within range

    """
    x = Prime_Number(30)  # here we calling function from Utility
    result = Prime_Palindrome(x)  # here we calling function from algorithms
    assert result == [11]
