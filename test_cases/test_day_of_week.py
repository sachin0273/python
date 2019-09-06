from Utility.utility import Day_Of_Week, load


def test_day_of_week_string():
    """

    :return: this test case used for checking day of week of given date

    """
    data = load("test.json")
    dat = data["test"][0]["day_of_week"]
    result = Day_Of_Week(dat[0]["input_day"], dat[0]["input_month"], dat[0]["input_year"])  # here we calling function
    # from Utility
    assert result == dat[0]["output"]


def test_day_of_week_space():
    """

    :return: this test case used for checking day of week of given date

    """
    data = load("test.json")
    dat = data["test"][0]["day_of_week"]
    result = Day_Of_Week(dat[1]["input_day"], dat[1]["input_month"], dat[1]["input_year"])  # here we calling function
    # from Utility
    assert result == dat[1]["output"]


def test_day_of_week_special_char():
    """

    :return: this test case used for checking day of week of given date

    """
    data = load("test.json")
    dat = data["test"][0]["day_of_week"]
    result = Day_Of_Week(dat[2]["input_day"], dat[2]["input_month"], dat[2]["input_year"])  # here we calling function
    # from Utility
    assert result == dat[2]["output"]


def test_day_of_week_int():
    """

    :return: this test case used for checking day of week of given date

    """
    data = load("test.json")
    dat = data["test"][0]["day_of_week"]
    result = Day_Of_Week(dat[3]["input_day"], dat[3]["input_month"], dat[3]["input_year"])  # here we calling function
    # from Utility
    assert result == dat[3]["output"]
