import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/NFLX.csv', encoding='cp949',usecols=['Date', 'Open', 'High', 'Low', 'Close'])
df.head()

# 2021년 이후 데이터 필터링
df['Date'] = pd.to_datetime(df['Date'])
filter_date = df[df['Date'] >= pd.to_datetime('2021-01-01')]
avg_data = df.groupby(filter_date['Date'].dt.to_period('M')).mean()

# x2 = avg_data
# print(type(avg_data))
plt.plot(avg_data['Date'],avg_data['Close'])
plt.xticks(rotation=45)


plt.title('Monthly Average Close Price')
plt.xlabel('Date')
plt.ylabel('Average Close Price')

plt.show()