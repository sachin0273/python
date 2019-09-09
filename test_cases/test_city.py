from Utility.utility import load
from OOPS.for_test import Test

Test = Test()


def test_city_string_input():
    data = load("test.json")
    dat = data["test"][0]["city"]
    result = Test.City(dat[0]["input"])
    assert result == dat[0]["output"]


def test_city_space_input():
    data = load("test.json")
    dat = data["test"][0]["city"]
    result = Test.City(dat[1]["input"])
    assert result == dat[1]["output"]


def test_city_spacial_char_input():
    data = load("test.json")
    dat = data["test"][0]["city"]
    result = Test.City(dat[2]["input"])
    assert result == dat[2]["output"]


def test_city_digit_input():
    data = load("test.json")
    dat = data["test"][0]["city"]
    result = Test.City(dat[3]["input"])
    assert result == dat[3]["output"]
