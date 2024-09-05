from twttr import shorten

def test_HAPPY():
    assert shorten("HAPPY") == "HPPY"

def test_Cs50():
    assert shorten("Cs50") == "Cs50"

def test_number():
    assert shorten("12345") == "12345"

def test_abcd():
    assert shorten("abcd") == "bcd"

def test_punc():
    assert shorten("Hi! there..") == "H! thr.."