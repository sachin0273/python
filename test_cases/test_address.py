from Utility.utility import load
from OOPS.for_test import Test

Test = Test()


def test_address_string_input():
    data = load("test.json")
    dat = data["test"][0]["address"]
    result = Test.Address(dat[0]["input"])
    assert result == dat[0]["output"]


def test_address_space_input():
    data = load("test.json")
    dat = data["test"][0]["address"]
    result = Test.Address(dat[1]["input"])
    assert result == dat[1]["output"]


def test_address_spacial_char_input():
    data = load("test.json")
    dat = data["test"][0]["address"]
    result = Test.Address(dat[2]["input"])
    assert result == dat[2]["output"]


def test_address_digit_input():
    data = load("test.json")
    dat = data["test"][0]["address"]
    result = Test.Address(dat[3]["input"])
    assert result == dat[3]["output"]


def test_address_actual_input():
    data = load("test.json")
    dat = data["test"][0]["address"]
    result = Test.Address(dat[4]["input"])
    assert result == dat[4]["output"]
