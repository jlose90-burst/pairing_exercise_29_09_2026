from lib.return_names import *

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

def test_4_names():
    result = return_names(['tisha','jon','fictional_friend','ben'])
    assert result == 'tisha, jon, fictional_friend & ben'