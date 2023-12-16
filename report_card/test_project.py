import pytest
from project import name_major, symbol_num, grading


#check the userinput name or major
def test_name_major():
    assert name_major("Kiran Bulan") == "Kiran Bulan"
    assert name_major("hello world") == "Hello World"
    assert name_major("science") == "Science"
    assert name_major("Bachelor in information technology") == "Bachelor In Information Technology"


#check for user_symbol number
def test_symbol_num():
    assert symbol_num(12345) == 12345
    assert symbol_num(123) == 123
    assert symbol_num(1) == 1


#check the grading
def test_grading():
    assert grading(90) == "A+"
    assert grading(85) == "A "
    assert grading(73) == "B+"
    assert grading(68) == "B "
    assert grading(57) == "C+"
    assert grading(48) == "C "
    assert grading(25) == "D "
    assert grading(15) == "F "
    assert grading(0)  == "F "


# test for value Error
def test_value_error():
    with pytest.raises(ValueError):
        name_major("")
        name_major("12344")

    with pytest.raises(ValueError):
        symbol_num("abcd")
        symbol_num("1236488952")
        symbol_num("")