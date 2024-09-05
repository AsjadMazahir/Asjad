# Implementing a Trading Strategy in Stock Market
#### Video Demo:  <URL https://youtu.be/kxLQrTHA3-k>
#### The brief description of the project is as follows:
1. The program takes the input of stock market data from csv file. The file contains Price, Vol., High, Low, Change %,\
Open, Date as columns. The file is loaded as pandas dateframe using pandas library.
2. Since only price and date data is required, we wil get rid of remaining columns using df.drop function.
3. The data contain in the csv files is the daily data of Pakistan Stock Exchange downloaded from investing.com.
4. The program contains three functions for calculating technical indicators namely \
Exponential Moving Average (EMA), Weighted Moving Average (WMA), and Moving Average Convergence Divergence (MACD)
5. Based on the values of technical indicator, the program makes buy and sell decision and calculates profit.

##### The strategy for trade is as follows:
1. Calculate n day EMA of closing prices. The parameter n is taken from user.
2. Calculate MACD(12,26,9) of closing prices. Also calculate EMA and MACD slope which are then added to the dataframe.
3. If EMA slope and MACD slope is positive then buy the stock.
4. If EMA slope is negative or MACD slope is negative then sell the stock.
5. If EMA slope is negative then wait for change in trend.
6. This strategy provides buy signals in nice uptrends while limiting drawdowns in case stock price reverses.

##### Implementation of the Strategy
1. There are three functions calc_ema, calc_wma, calc_macd.
2. The programs reads csv file into pandas dataframe.
3. The functions calc_ema, calc_wma, and calc_macd calculates the Exponential Moving Average (EMA), \
Weighted Moving Average (WMA) and Moving Average Convergence Divergence (MACD) indicator respectively.
4. The input parameters of the function contains a list of stock price data (taken from csv file) and \
parameters for technical indicators. The details of the indicators can be found in the links below.\
    - [EMA](https://www.investopedia.com/ask/answers/071414/whats-difference-between-moving-average-and-weighted-moving-average.asp)
    - [MACD](https://www.investopedia.com/terms/m/macd.asp#:~:text=Key%20Takeaways-,Moving%20average%20convergence%2Fdivergence%20(MACD)%20is%20a%20technical%20indicator,EMA%20of%20the%20MACD%20line)
5. A new column "Long" is added to dataframe which gives buy and sell signals based on values of technical indicators.\
For instance, if EMA is positive and MACD if positive than the signal is BUY. Similarly if EMA is negative and MACD is negative then the signal is SELL.
6. Another column "Position" is added to the dataframe that indicates the OPEN and CLOSE positions based on \
the "Long" columnn.
7. For calculating profits, a new dataframe is created that contains data for only OPEN and CLOSE positions.
8. The profit is calculated based on the price of the subsequent OPEN and CLOSE positions. It should be noted that \
one pair of OPEN and CLOSE position is marked as a single trade. The profits of all the trades are appended to a list \
and then added to get the sum of profits.
9. The above strategy can also be applied using Weighted Moving Average (WMA) by using calc_wma function.
10. Since the EMA parameter is taken from user, different input parameters can be tried to test which parameter \
generated the maximum profit.
