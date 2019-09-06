from Utility.utility import Bubble_Sort, load


def test_bubble_sort_string():
    """

    :return: this test case used for sorting string of list
    """
    data = load("test.json")
    dat = data["test"][0]["bubble_sort"]
    result = Bubble_Sort(dat[0]["input"])  # here we calling function from Utility
    assert result == dat[0]["output"]


def test_bubble_sort_space():
    """

    :return: this test case used for sorting string of list
    """
    data = load("test.json")
    dat = data["test"][0]["bubble_sort"]
    result = Bubble_Sort(dat[1]["input"])  # here we calling function from Utility
    assert result == dat[1]["output"]


def test_bubble_sort_spacial_char():
    """

    :return: this test case used for sorting string of list
    """
    data = load("test.json")
    dat = data["test"][0]["bubble_sort"]
    result = Bubble_Sort(dat[2]["input"])  # here we calling function from Utility
    assert result == dat[2]["output"]


def test_bubble_sort_spacial_digit():
    """

    :return: this test case used for sorting string of list
    """
    data = load("test.json")
    dat = data["test"][0]["bubble_sort"]
    result = Bubble_Sort(dat[3]["input"])  # here we calling function from Utility
    assert result == dat[3]["output"]


def test_bubble_sort_list():
    """

    :return: this test case used for sorting string of list
    """
    data = load("test.json")
    dat = data["test"][0]["bubble_sort"]
    result = Bubble_Sort(dat[4]["input"])  # here we calling function from Utility
    assert result == dat[4]["output"]
