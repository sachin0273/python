from Utility.utility import Binary_Search, load


def test_binary_search_pass():
    """

    :return: in this test case we are checking word is present in list or not
    """
    search_from = ["sachin", "ght", "jk", "madam"]
    data = load("test.json")
    dat = data["test"][0]["binary_search"]
    result = Binary_Search(search_from, dat[0]["input"])  # here we calling function from Utility
    assert result == dat[0]["output"]


def test_binary_search_fail():
    """

    :return: in this test case we are checking word is present in list or not
    """
    search_from = ["sachin", "ght", "jk", "madam"]
    data = load("test.json")
    dat = data["test"][0]["binary_search"]
    result = Binary_Search(search_from, dat[1]["input"])  # here we calling function from Utility
    assert result == dat[1]["output"]


def test_binary_search_fail2():
    """

    :return: in this test case we are checking word is present in list or not
    """
    search_from = ["sachin", "ght", "jk", "madam"]
    data = load("test.json")
    dat = data["test"][0]["binary_search"]
    result = Binary_Search(search_from, dat[2]["input"])  # here we calling function from Utility
    assert result == dat[2]["output"]


def test_binary_search_fail3():
    """

    :return: in this test case we are checking word is present in list or not
    """
    search_from = ["sachin", "ght", "jk", "madam"]
    data = load("test.json")
    dat = data["test"][0]["binary_search"]
    result = Binary_Search(search_from, dat[3]["input"])  # here we calling function from Utility
    assert result == dat[3]["output"]
