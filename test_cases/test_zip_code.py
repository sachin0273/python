from Utility.utility import load
from OOPS.for_test import Test

Test = Test()


def test_zip_code_string_input():
    data = load("test.json")
    dat = data["test"][0]["zip_code"]
    result = Test.Zip_Code(dat[0]["input"])
    assert result == dat[0]["output"]


def test_zip_code_space_input():
    data = load("test.json")
    dat = data["test"][0]["zip_code"]
    result = Test.Zip_Code(dat[1]["input"])
    assert result == dat[1]["output"]


def test_zip_code_spacial_char_input():
    data = load("test.json")
    dat = data["test"][0]["zip_code"]
    result = Test.Zip_Code(dat[2]["input"])
    assert result == dat[2]["output"]


def test_zip_code_digit_input():
    data = load("test.json")
    dat = data["test"][0]["zip_code"]
    result = Test.Zip_Code(dat[3]["input"])
    assert result == dat[3]["output"]


def test_zip_code_actual_input():
    data = load("test.json")
    dat = data["test"][0]["zip_code"]
    result = Test.Zip_Code(dat[4]["input"])
    assert result == dat[4]["output"]
