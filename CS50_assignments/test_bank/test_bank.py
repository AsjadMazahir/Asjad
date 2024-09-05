from bank import value

def test_hello():
    assert value("hello") == 0

def test_Hello():
    assert value("Hello") == 0

def test_hi():
    assert value("hi") == 20

def test_Hi():
    assert value("Hi") == 20

def test_good_morning():
    assert value("good morning") == 100