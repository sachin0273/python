from Utility.utility import load
from OOPS.for_test import Test

Test = Test()


def test_full_name_string_input():
    data = load("test.json")
    dat = data["test"][0]["full_name"]
    result = Test.Full_Name(dat[0]["input"])
    assert result == dat[0]["output"]


def test_full_name_space_input():
    data = load("test.json")
    dat = data["test"][0]["full_name"]
    result = Test.Full_Name(dat[1]["input"])
    assert result == dat[1]["output"]


def test_full_name_spacial_char_input():
    data = load("test.json")
    dat = data["test"][0]["full_name"]
    result = Test.Full_Name(dat[2]["input"])
    assert result == dat[2]["output"]


def test_full_name_digit_input():
    data = load("test.json")
    dat = data["test"][0]["full_name"]
    result = Test.Full_Name(dat[3]["input"])
    assert result == dat[3]["output"]


def test_full_name_actual_input():
    data = load("test.json")
    dat = data["test"][0]["full_name"]
    result = Test.Full_Name(dat[4]["input"])
    assert result == dat[4]["output"]
