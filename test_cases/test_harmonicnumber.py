from Utility.utility import Harmonic_Number, load


def test_check_harmonic_string():
    """

    :return: in this test case we check harmonic addition of given nth number

    """
    data = load("test.json")
    dat = data["test"][0]["harmonic_number"]
    result = Harmonic_Number(dat[0]["input"])  # here we calling function from Utility
    assert result == dat[0]["output"]


def test_check_harmonic_space():
    """

    :return: in this test case we check harmonic addition of given nth number

    """
    data = load("test.json")
    dat = data["test"][0]["harmonic_number"]
    result = Harmonic_Number(dat[1]["input"])  # here we calling function from Utility
    assert result == dat[1]["output"]


def test_check_harmonic_spacial_char():
    """

    :return: in this test case we check harmonic addition of given nth number

    """
    data = load("test.json")
    dat = data["test"][0]["harmonic_number"]
    result = Harmonic_Number(dat[2]["input"])  # here we calling function from Utility
    assert result == dat[2]["output"]


def test_check_harmonic_int():
    """

    :return: in this test case we check harmonic addition of given nth number

    """
    data = load("test.json")
    dat = data["test"][0]["harmonic_number"]
    result = Harmonic_Number(dat[3]["input"])  # here we calling function from Utility
    assert result == dat[3]["output"]
