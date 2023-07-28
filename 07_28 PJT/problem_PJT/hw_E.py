import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/NFLX.csv', encoding='cp949',usecols=['Date', 'Open', 'High', 'Low', 'Close'])
df.head()

# 2021년 이후 데이터 필터링
df['Date'] = pd.to_datetime(df['Date'])
filter_date = df[df['Date'] >= '2022-01-01']

plt.plot(filter_date['Date'],filter_date['High'],label='High')
plt.plot(filter_date['Date'],filter_date['Low'],label='Low')
plt.plot(filter_date['Date'],filter_date['Close'],label='Close')
plt.xticks(rotation=45)
plt.legend()


plt.title('High, Low, and Close Price since january 2022')
plt.xlabel('Date')
plt.ylabel('Price')

plt.show()