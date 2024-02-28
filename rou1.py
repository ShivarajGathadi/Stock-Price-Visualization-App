import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock price app

shown are the stock closing price and volume of google!
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start = '2019-1-26', end = '2024-1-27')

st.line_chart(tickerDf.Close)
st.write("""
Volume of the Chart""")
st.line_chart(tickerDf.Volume)

st.markdown("""
<style>
.top-right {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 18px;
    colour: #636363;
}
</style>
<div class="top-right">Shivaraj Gathadi</div>
""",
unsafe_allow_html=True
)