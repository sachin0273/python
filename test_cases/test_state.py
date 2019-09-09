from Utility.utility import load
from OOPS.for_test import Test

Test = Test()


def test_state_string_input():
    data = load("test.json")
    dat = data["test"][0]["state"]
    result = Test.State(dat[0]["input"])
    assert result == dat[0]["output"]


def test_state_space_input():
    data = load("test.json")
    dat = data["test"][0]["state"]
    result = Test.State(dat[1]["input"])
    assert result == dat[1]["output"]


def test_state_spacial_char_input():
    data = load("test.json")
    dat = data["test"][0]["state"]
    result = Test.State(dat[2]["input"])
    assert result == dat[2]["output"]


def test_state_digit_input():
    data = load("test.json")
    dat = data["test"][0]["state"]
    result = Test.State(dat[3]["input"])
    assert result == dat[3]["output"]
