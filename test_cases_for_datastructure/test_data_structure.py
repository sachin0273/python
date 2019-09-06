"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Purpose: in this module created different test cases for data structure functions positive as well negative
author:  Sachin Shrikant Jadhav
since :  30-08-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

from data_structure.for_test import linked_test

"""here we creating object"""

linked = linked_test()
data = [20, 24, 56, 78]
for dat in data:
    linked.add_to_start(dat)


def test_start_add():
    """

    :return: this test used for add_to start function of linked list for true case

    """
    result = linked.display()

    assert [78, 56, 24, 20] == result


def test_fail_add_to_start():
    """

    :return: this test used for add_to start function of linked list for false case

    """
    result = linked.display()

    assert result != [56, 24, 20]


def test_last_add():
    """

    :return: this test used for add_to last function of linked list for true case

    """
    linked.add_to_last(12)
    result = linked.display()

    assert [78, 56, 24, 20, 12] == result


def test_last_add_fail():
    """

    :return: this test used for add_to last function of linked list for false case

    """
    result = linked.display()

    assert result != [34, 89, 56]


def test_delete_start():
    """

    :return: this test used for delete_to_start function of linked list for true case

    """
    linked.delete_to_start()
    result = linked.display()
    assert [56, 24, 20, 12] == result


def test_delete_start_fail():
    """

    :return: this test used for delete_to_start function of linked list for false case

    """
    linked.delete_to_start()
    result = linked.display()
    assert result != [67, 90]


def test_deelete_last():
    """

    :return:this test used for delete_to_last function of linked list for true case

    """
    linked.delete_to_last()
    result = linked.display()
    assert [24, 20] == result


def test_deelete_last_fail():
    """

    :return:this test used for delete_to_start function of linked list for false case

    """
    linked.delete_to_last()
    result = linked.display()
    assert [66, 99, 63, 43] != result


def test_search():
    """

    :return:this test used for search function of linked list for true case

    """
    result = linked.search(24)
    assert True == result


def test_search_fail():
    """

    :return:this test used for search function of linked list for fail case

    """
    result = linked.search(24)
    assert False != result


def test_delete_at_position():
    """

    :return: his test used for delete_element_by_position function of linked list for true case

    """
    linked.add_to_last(35)
    linked.add_to_last(45)
    linked.delete_at_position(2)
    result = linked.display()
    assert [24, 35] == result


def test_insert_at_position():
    """

    :return:is test used for insert at position  function of linked list for true case

    """
    linked.insert_at_position(2, 67)
    result = linked.display()
    assert [24, 35, 67] == result


def test_insert_at_position_fail():
    """

    :return:is test used for insert at position  function of linked list for false  case

    """
    linked.insert_at_position(3, 68)
    result = linked.display()
    assert [24, 35, 67] != result


def test_search_if_found_remove_else_add():
    """

    :return:is test is used for search element if found remove else add in linked list for true case

    """
    linked.search_element_add_delete(67)
    result = linked.display()
    assert [24, 35, 68] == result


def test_search_if_found_remove_else_add_failcase():
    """

    :return:is test is used for search element if found remove else add in linked list for fail case

    """
    linked.search_element_add_delete(67)
    result = linked.display()
    assert [24, 35, 68] != result


def test_delete_last_save():
    """

    :return:is test is used for delete last element and return  in linked list for true case

    """
    result = linked.delete_to_last_save()
    assert 67 == result


def test_delete_last_save_failcase():
    """

    :return:is test is used for delete last element and return  in linked list for fail case

    """
    result = linked.delete_to_last_save()
    assert 67 != result


def test_delete_start_save():
    """

    :return: is test is used for delete first element and return  in linked list for true case

    """
    result = linked.delete_to_start_save()
    assert 24 == result


def test_delete_start_save_failcase():
    """

    :return: is test is used for delete first element and return  in linked list for true case

    """
    result = linked.delete_to_start_save()
    assert 24 != result
