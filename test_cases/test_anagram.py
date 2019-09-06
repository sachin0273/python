from Utility.utility import Is_Anagram, load


def test_anagram():
    """

    :return: this test case is used for checking anagram of string
    """
    data = load("test.json")
    dat = data["test"][0]["anagram"]
    result = Is_Anagram(dat[0]["string1"], dat[0]["string2"])
    assert result == dat[0]["output"]


def test_anagram_pass():
    """

    :return: this test case is used for checking anagram of string
    """
    data = load("test.json")
    dat = data["test"][0]["anagram"]
    result = Is_Anagram(dat[1]["string1"], dat[1]["string2"])
    assert result == dat[1]["output"]


def test_anagram_pass2():
    """

    :return: this test case is used for checking anagram of string
    """
    data = load("test.json")
    dat = data["test"][0]["anagram"]
    result = Is_Anagram(dat[2]["string1"], dat[2]["string2"])
    assert result == dat[2]["output"]


def test_anagram_fail():
    """

    :return: this test case is used for checking anagram of string
    """
    data = load("test.json")
    dat = data["test"][0]["anagram"]
    result = Is_Anagram(dat[3]["string1"], dat[3]["string2"])
    assert result == dat[3]["output"]
