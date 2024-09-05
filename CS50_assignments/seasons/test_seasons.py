from seasons import get_days, convert_to_words
import pytest

def test_get_days1():
    assert (get_days("2021-10-29") == 365)

def test_get_days2():
    with pytest.raises(SystemExit):
        get_days("October 29 2021")

def test_convert_to_words():
    assert (convert_to_words(1234) == "One thousand, two hundred thirty-four")