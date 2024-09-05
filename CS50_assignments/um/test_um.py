from um import count
import pytest

def test_um1():
    assert count("um") == 1

def test_um2():
    assert count("Um... you must be right... ummmm") == 1

def test_um3():
    assert count("UM.. um") == 2

def test_um4():
    assert count("Um-er") == 1