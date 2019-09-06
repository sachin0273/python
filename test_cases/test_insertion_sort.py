from Utility.utility import Insertion_Sort


def test_insertion_sort():
    """

    :return: in this test case we are check insertion sort

    """
    input = [1, 89, 70, 46, 4]
    result = Insertion_Sort(input)  # here we calling function from  Utility
    assert result == [1, 4, 46, 70, 89]
