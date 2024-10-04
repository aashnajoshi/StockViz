import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
from datetime import datetime

st.title("Stock Price Viewer")
end_date = pd.Timestamp.today(tz='America/New_York').ceil('D')
# start_date = end_date - pd.Timedelta(7,'D') # Get the last 7 days
start_date = end_date - pd.Timedelta(365,'D') # Get the last 365 days

# Microsoft (MSFT)
st.header("Microsoft (MSFT)")
msft = yf.Ticker("MSFT")
data = msft.history(start=start_date, end=end_date, interval='1d').reset_index()

# Create a plot for Microsoft stock prices
fig = go.Figure(data=go.Scatter(x=data['Date'], y=data['Close'], mode='lines'))
fig.update_layout(
    title='Microsoft (MSFT)',
    title_x=0.5,
    autosize=False,
    width=800,
    height=500,
    xaxis=dict(
        rangeselector=dict(
            buttons=[
                dict(count=30, label="30D", step="day", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1Y", step="year", stepmode="backward")])))
st.plotly_chart(fig)

# Salesforce (CRM)
st.header("Salesforce (CRM)")
crm = yf.Ticker("CRM")
crm_data = crm.history(start=start_date, end=end_date, interval='1d').reset_index()

# Create a plot for Salesforce stock prices
crm_fig = go.Figure(data=go.Scatter(x=crm_data['Date'], y=crm_data['Close'], mode='lines'))
crm_fig.update_layout(
    title='Salesforce (CRM)',
    title_x=0.5,
    autosize=False,
    width=800,
    height=600,
    xaxis=dict(
        rangeselector=dict(
            buttons=[
                dict(count=1, label="1H", step="hour", stepmode="backward"),
                dict(label='1D', step="all")])))
st.plotly_chart(crm_fig)

now = datetime.now().strftime("%B %d, %Y at %H:%M")
st.write(f'Last run on {now} UTC')
