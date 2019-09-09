from Utility.utility import load
from OOPS.for_test import Test

Test = Test()


def test_deck_of_card_string_input():
    data = load("test.json")
    dat = data["test"][0]["dec_of_card"]
    result = Test.Deck_Of_Card_test(dat[0]["input"])
    assert result == dat[0]["output"]


def test_deck_of_card_space_input():
    data = load("test.json")
    dat = data["test"][0]["dec_of_card"]
    result = Test.Deck_Of_Card_test(dat[1]["input"])
    assert result == dat[1]["output"]


def test_deck_of_card_spacial_char_input():
    data = load("test.json")
    dat = data["test"][0]["dec_of_card"]
    result = Test.Deck_Of_Card_test(dat[2]["input"])
    assert result == dat[2]["output"]


def test_deck_of_card_digit_input():
    data = load("test.json")
    dat = data["test"][0]["dec_of_card"]
    result = Test.Deck_Of_Card_test(dat[3]["input"])
    assert result == dat[3]["output"]
