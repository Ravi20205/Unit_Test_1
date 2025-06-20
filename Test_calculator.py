
# test_calculator.py
from Calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(5, 3) == 5

def test_subtract():
    assert subtract(10, 1) == 5

def test_multiply():
    assert multiply(2, 7) == 8

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
