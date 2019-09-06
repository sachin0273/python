from Utility.utility import User_Name, load


def test_username_string():
    """

    :return: this test used for checking length of input and replaced template output

    """
    data = load("test.json")
    dat = data["test"][0]["username_input"]
    result = User_Name(dat[0]["input"])  # here we calling function from Utility
    assert result == dat[0]["output"]


def test_username_space():
    """

    :return: this test used for checking length of input and replaced template output

    """
    data = load("test.json")
    dat = data["test"][0]["username_input"]
    result = User_Name(dat[1]["input"])  # here we calling function from Utility
    assert result == dat[1]["output"]


def test_username_char():
    """

    :return: this test used for checking length of input and replaced template output

    """
    data = load("test.json")
    dat = data["test"][0]["username_input"]
    result = User_Name(dat[2]["input"])  # here we calling function from Utility
    assert result == dat[2]["output"]


def test_username_digit():
    """

    :return: this test used for checking length of input and replaced template output

    """
    data = load("test.json")
    dat = data["test"][0]["username_input"]
    result = User_Name(dat[3]["input"])  # here we calling function from Utility
    assert result == dat[3]["output"]
