#pip install yfinance
#pip install plotly==5.6.

import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=720)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('AMZN',
                   start=start_date,
                   end=end_date,
                   progress=False)
print(data.head())

import plotly.express as px
figure = px.line(data, x = data.index,
                 y = "Close",
                 title = "Time Series Analysis (LinePlot)")
figure.show()

import plotly.graph_objects as go
figure = go.Figure(data=[go.Candlestick(x = data.index, 
                                        open = data["Open"],
                                        high = data["High"],
                                        low = data["Low"],
                                        close = data["Close"])])

figure.update_layout(title = "Time Series Analysis (Candlestick Chart)",
                     xaxis_rangeslider_visible = False)
figure.show()


# Time Series Analysis
figure = go.Figure(data = [go.Candlestick(x = data.index,
                                        open = data["Open"], 
                                        high = data["High"],
                                        low = data["Low"], 
                                        close = data["Close"])])
figure.update_layout(title = "Time Series Analysis (Candlestick Chart with Buttons and Slider)")

figure.update_xaxes(
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = "1m", step = "month", stepmode = "backward"),
            dict(count = 6, label = "6m", step = "month", stepmode = "backward"),
            dict(count = 1, label = "YTD", step = "year", stepmode = "todate"),
            dict(count = 1, label = "1y", step = "year", stepmode = "backward"),
            dict(step = "all")
        ])
    )
)
figure.show()