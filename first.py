import yfinance as yf
import streamlit as sl
import pandas as pd

sl.title('My Finance App')
df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = df.Symbol.to_list()
comps = ['Price Comparison', 'Performance Comparison']
dropdown = sl.multiselect('Choose your  ticker', tickers)
start = sl.date_input('Start date', pd.to_datetime('2019-01-01'))
end = sl.date_input('End date', pd.to_datetime('today'))




def relret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() -1
    cumret = cumret.fillna(0)
    return cumret



if len(dropdown) > 0:
    df = relret(yf.download(dropdown, start, end)['Adj Close'])
    sl.line_chart(df)
    mc = dropdown.info['marketCap']
    fth = dropdown.info['fiftyTwoWeekHigh']
    ftl = dropdown.info['fiftyTwoWeekLow']
    pr = dropdown.info['payoutRatio']
    yi = dropdown.info['yield']
    pcl = dropdown.info['previousClose']
    ptb =dropdown.info['priceToBook']
    d = {'Market Cap': [mc], 'Fifty Two Week High': [fth], 'Fifty Two Week Low': [ftl], 'Price to Book': [ptb], 'Previous Close': [pcl], 'Payout Ratio': [pr], 'Yield': [yi]}
    df = pd.DataFrame(data=d)

    sl.table(df)