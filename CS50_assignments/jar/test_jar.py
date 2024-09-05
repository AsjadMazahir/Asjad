from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar(7)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(6)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.deposit(5)

def test_withdrar():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(6)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(5)