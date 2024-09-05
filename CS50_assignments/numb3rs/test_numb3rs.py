from numb3rs import validate

def test_string():
    assert validate("cat") == False

def test_largernumber():
    assert validate("111.222.333.111") == False

def test_number():
    assert validate("222.222.222.222") == True

def test_smallnumber():
    assert validate("111.111.111.-22") == False