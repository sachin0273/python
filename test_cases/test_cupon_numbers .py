from Utility.utility import Coupn, load


def test_check_string():
    """

    :param N: number of distinct coupn
    :return: this test case used for checking number of distinct coupn
    """
    data = load("test.json")
    dat = data["test"][0]["coupon_number"]
    result = Coupn(dat[0]["input"])  # here we calling function from Utility
    assert result == dat[0]["output"]


def test_check_space():
    """

    :param N: number of distinct coupn
    :return: this test case used for checking number of distinct coupn
    """
    data = load("test.json")
    dat = data["test"][0]["coupon_number"]
    result = Coupn(dat[1]["input"])  # here we calling function from Utility
    assert result == dat[1]["output"]


def test_check_spacial_char():
    """

    :param N: number of distinct coupn
    :return: this test case used for checking number of distinct coupn
    """
    data = load("test.json")
    dat = data["test"][0]["coupon_number"]
    result = Coupn(dat[2]["input"])  # here we calling function from Utility
    assert result == dat[2]["output"]


def test_check_integer():
    """

    :param N: number of distinct coupn
    :return: this test case used for checking number of distinct coupn
    """
    data = load("test.json")
    dat = data["test"][0]["coupon_number"]
    result = Coupn(dat[3]["input"])  # here we calling function from Utility
    assert len(result) == dat[3]["output"]
