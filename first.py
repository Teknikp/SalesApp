import yfinance as yf
import streamlit as sl
import pandas as pd

sl.title('My little Finance App')
df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = df.Symbol.to_list()
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