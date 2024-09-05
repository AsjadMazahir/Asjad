"""
This program
(1) Get the list of stock symbols from given file
(2) Sort the data in the required format
(3) Calculated the exponential moving average (EMA), Weighted moving average (WMA), MACD of the prices
(4) Based on technical indicators, analyse whether to buy or sell
(5) Compute the average return and compare it to buy and hold strategy
"""
import numpy as np
import datetime
import pandas as pd

def main():
    #(Importing Data)
    df= pd.read_csv("AVN_Historical_Data.csv")
    df = df.drop(columns=['Vol.', 'High', 'Low', 'Change %', 'Open'])
    df = df[::-1]
    # Converting date column data type
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.reset_index(drop=True)
    # Getting Exponential MA parameter from user
    try:
        n = int(input("Please input the EMA parameter: "))
    except ValueError:
        print("EMA parameter must be an integer")

    data_list = df['Price'].to_list()
    # Calculating EMA, MACD
    df[f'EMA{n}'] = calc_ema(data_list, n)
    df['MACD_hist'] = calc_macd(data_list, 12, 26, 9)[2]
    df['MACD_signal'] = calc_macd(data_list, 12, 26, 9)[1]
    df['MACD_line'] = calc_macd(data_list, 12, 26, 9)[0]

    # Calculating slope of EMA12, MACD_hist
    df[f'EMA{n}_slope'] = df[f'EMA{n}'].diff()
    df['MACD_hist_slope'] = df['MACD_hist'].diff()
    print("Adding EMA, MACD and their slopes to dataframe")
    print(df.head(10))

    # dropping the initial missing values of MACD_hist_slope
    # since our Buy and Sell calls are based on MACD_hist_slope
    print("Dropping null values from MACD histogram slope")
    df2 = df.dropna()
    print(df2.head(10))

    # Giving BUY and SELL calls
    df2.loc[(df2[f'EMA{n}_slope'] > 0) & (df2['MACD_hist_slope'] > 0), 'Call'] = "BUY"
    df2.loc[(df2[f'EMA{n}_slope'] < 0) | (df2['MACD_hist_slope'] < 0), 'Call'] = "SELL"

    # Taking long positions based on first buy and subsequent sell calls
    df2.loc[(df2['Call'] == 'BUY') & (df2['Call'].shift() != 'BUY'), 'Long'] = 'OPEN'
    df2.loc[(df2['Call'] == 'SELL') & (df2['Call'].shift() != 'SELL'), 'Long'] = 'CLOSE'
    print("Giving BUY and SELL calls based on EMA and MACD slope")
    print(df2.head(10))

    # Getting data with only OPEN and CLOSE position
    df3 = df2[(df2['Long'] == 'OPEN') | (df2['Long'] == 'CLOSE')]
    df3 = df3.reset_index(drop=True)
    print("Getting dataframe with only OPEN and CLOSE position")
    print(df3)

    # Calculating profit/loss
    profits = []
    for i in range(len(df3)):
        if df3['Long'][i] == 'CLOSE' and i > 0:
            p = (df3['Price'][i] - df3['Price'][i-1])*100/(df3['Price'][i-1])
            p = round(p,2)
            profits.append(p)
    print("Profits: ", profits)
    print("Total Profit(%): ", sum(profits))

def calc_ema(data_list, n):
    """
    This function takes list of stock prices and no of days (n) as parameters and
    returns a list of exponential moving averages for n days
    """
    k = 2/(n+1)
    new_list = [None for _ in range(n - 1)]

    for i in range(len(data_list) - n + 1):
        if new_list[i + n - 2] == None:
            EMA_p = sum(data_list[i:i + n])/n
            EMA_t = EMA_p
        else:
            EMA_p = new_list[i + n - 2]
            EMA_t = data_list[i+n-1] * k + (1-k) * EMA_p

        EMA_t = round(EMA_t, 4)
        new_list.append(EMA_t)

    return new_list

def calc_wma(data_list, n):
    """
    This function takes list of stock prices and no of days (n) as parameters and
    returns a list of weighted moving averages for n days
    """
    new_list = [None for _ in range(n-1)]

    for i in range(len(data_list) - n + 1):
        sum = 0
        for j in range(n):
            x = data_list[i+j]*(j+1)
            sum = sum + x

        WMA = (sum * 2)/(n*(n+1))
        WMA = round(WMA, 4)
        new_list.append(WMA)

    return new_list

def calc_macd(data_list, n1, n2, n3):
    """
    This function calculated MACD indicator for given set of MACD parameters
    """
    EMAn1 = calc_ema(data_list, n1)
    EMAn2 = calc_ema(data_list, n2)
    MACD_line = []
    for x, y in zip(EMAn1, EMAn2):
        if x == None or y == None:
            MACD_line.append(None)
        else:
            MACD_line.append(round((x-y), 4))
    MACD_signal = calc_ema(MACD_line[n2-1:], n3)
    MACD_signal = [None for num in range(n2-1)] + MACD_signal

    MACD_hist = []
    for i, j in zip(MACD_line, MACD_signal):
        if i == None or j == None:
            MACD_hist.append(None)
        else:
            MACD_hist.append(round((i-j), 4))

    return (MACD_line, MACD_signal, MACD_hist)

if __name__ == "__main__":
    main()
