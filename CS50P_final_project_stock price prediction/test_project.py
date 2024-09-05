from project import calc_ema, calc_wma, calc_macd

def test_calc_ema():
    data = [11, 11, 11.4, 11.7, 12.1, 12.4, 12.6, 12, 13, 13.2, 12, 12]
    n = 5
    assert calc_ema(data, n) == [None, None, None, None, 11.44, 11.76, 12.04, 12.0267, 12.3511, 12.6341, 12.4227, 12.2818]

def test_calc_wma():
    data = [11, 11, 11.4, 11.7, 12.1, 12.4, 12.6, 12, 13, 13.2, 12, 12]
    n = 5
    assert calc_wma(data, n) == [None, None, None, None, 11.6333, 11.9533, 12.2467, 12.2333, 12.5133, 12.7733, 12.56, 12.3733]

def test_calc_macd():
    data = [11, 11, 11.4, 11.7, 12.1, 12.4, 12.6, 12, 13, 13.2, 12, 12, 14, 12, 11]
    n1 = 4
    n2 = 8
    n3 = 3
    assert calc_macd(data, n1, n2, n3)[0] == [None, None, None, None, None, None, None, 0.3413, 0.4226, 0.4585, 0.2211, 0.0907, 0.3774, 0.1221, -0.1857]


