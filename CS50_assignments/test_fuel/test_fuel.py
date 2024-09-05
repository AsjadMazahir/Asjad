from fuel import convert, gauge
import pytest

def test_convert_zero():

    with pytest.raises(ZeroDivisionError):
        convert ("1 / 0")

def test_convert_frac():
    assert convert("1/4") == 25
    assert convert("3/4") == 75

def test_convert_value():
    with pytest.raises(ValueError):
        convert("5/4")

def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("5.4/7")

def test_gauge1():
    assert(gauge(70)) == "70%"

def test_gauge2():
    assert(gauge(1)) == "E"

def test_gauge3():
    assert(gauge(99)) == "F"