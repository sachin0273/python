from Utility.utility import load
from OOPS.for_test import Test

Test = Test()


def test_phone_number_string_input():
    data = load("test.json")
    dat = data["test"][0]["phone_number"]
    result = Test.Phone_Number(dat[0]["input"])
    assert result == dat[0]["output"]


def test_phone_number_space_input():
    data = load("test.json")
    dat = data["test"][0]["phone_number"]
    result = Test.Phone_Number(dat[1]["input"])
    assert result == dat[1]["output"]


def test_phone_number_spacial_char_input():
    data = load("test.json")
    dat = data["test"][0]["phone_number"]
    result = Test.Phone_Number(dat[2]["input"])
    assert result == dat[2]["output"]


def test_phone_number_digit_input():
    data = load("test.json")
    dat = data["test"][0]["phone_number"]
    result = Test.Phone_Number(dat[3]["input"])
    assert result == dat[3]["output"]


def test_phone_number_input():
    data = load("test.json")
    dat = data["test"][0]["phone_number"]
    result = Test.Phone_Number(dat[4]["input"])
    assert result == dat[4]["output"]
