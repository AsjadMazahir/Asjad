from working import convert
import pytest

def test_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_3():
    assert convert("2:30 PM to 6:30 PM") == "14:30 to 18:30"

def test_4():
    with pytest.raises(ValueError):
        convert("2:30 PM - 6:30 PM")

def test_5():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_6():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")