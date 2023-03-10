"""
test_check_ip_func.py file!
"""

from example_test import check_ip

def test_check_ip_correct_10_1_1_1():
    assert (
        check_ip("10.1.1.1") == True
    ), "При правильном IP, функция должна возвращать True"


def test_check_ip_correct_180_10_1_1():
    assert (
        check_ip("180.10.1.1") == True
    ), "При правильном IP, функция должна возвращать True"

def test_check_in_wrong_octet():
    assert (
        check_ip("10.400.1.1") == False
    ), "При неправильном IP, функция должна возврашать False"

def test_check_ip_wrong_number_of_octets():
    assert (
        check_ip('10.1.1') == False
    ), "При неправильном IP, функция должна возвращать False"
    