from Utility.utility import Prime_Number, load


def test_prime_string():
    """

    :return: in this test case we are checking prime number of given range

    """
    data = load("test.json")
    dat = data["test"][0]["prime_number"]
    result = Prime_Number(dat[0]["input"])  # here we calling function from Utility
    assert result == dat[0]["output"]


def test_prime_space():
    """

    :return: in this test case we are checking prime number of given range

    """
    data = load("test.json")
    dat = data["test"][0]["prime_number"]
    result = Prime_Number(dat[1]["input"])  # here we calling function from Utility
    assert result == dat[1]["output"]


def test_prime_spacial_char():
    """

    :return: in this test case we are checking prime number of given range

    """
    data = load("test.json")
    dat = data["test"][0]["prime_number"]
    result = Prime_Number(dat[2]["input"])  # here we calling function from Utility
    assert result == dat[2]["output"]


def test_prime_string_int():
    """

    :return: in this test case we are checking prime number of given range

    """
    data = load("test.json")
    dat = data["test"][0]["prime_number"]
    result = Prime_Number(dat[3]["input"])  # here we calling function from Utility
    assert result == dat[3]["output"]
