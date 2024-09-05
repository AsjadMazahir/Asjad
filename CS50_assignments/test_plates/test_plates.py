from plates import is_valid

def test_valid1():
    assert is_valid("CS50") == True

def test_valid2():
    assert is_valid("HELLO") == True

def test_num_not_zero():
    assert is_valid("CS05") == False

def test_no_punct():
    assert is_valid("PI3.14") == False
    assert is_valid("PLATE:") == False

def test_num_at_end():
    assert is_valid("CS50P") == False

def test_length_shorter():
    assert is_valid("H") == False

def test_length_longer():
    assert is_valid("OUTATIME") == False

def test_alpha():
    assert is_valid("A555") == False