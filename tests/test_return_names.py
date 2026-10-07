from lib.return_names import *
import pytest

"""
test two names to see if they are joined with an &
"""
def test_plain_names_test_of_2():
    result = return_names(['tisha','jon'])
    assert result == "tisha & jon"

"""
test one name to see if it outputs one name
"""
def test_one_loner():
    result = return_names(['jon'])
    assert result == 'jon'
"""
test empty list to see if returns empty string
"""
def test_empty_list():
    result = return_names([])
    assert result == ''

"""
test 3 names to see if they are joined with a , an &
"""
def test_3_names():
    result = return_names(['tisha','jon','fictional_friend'])
    assert result == 'tisha, jon & fictional_friend'

"""
test 4 names to see if they are joined with a , an &
"""
def test_4_names():
    result = return_names(['tisha','jon','fictional_friend','ben'])
    assert result == 'tisha, jon, fictional_friend & ben'

"""
test input not being a list
"""
def test_not_a_list():
    with pytest.raises(Exception) as error:
        return_names('tisha, jon')
    assert str(error.value) == "Please enter a list"


"""
test int in list
"""
def test_int_in_list():
    with pytest.raises(TypeError) as error:
        return_names(['tisha','jon',3])
    assert str(error.value) == "Please only give 1 list of strings"

"""
test list in a list
"""
def test_list_in_a_list():
    with pytest.raises(TypeError) as error:
        return_names(['tisha','jon',['some friends']])
    assert str(error.value) == "Please only give 1 list of strings"