import csv
import numpy as np
import pandas as pd

df = pd.read_csv('data/NFLX.csv', encoding='cp949', usecols= ['Date', 'Open', 'High', 'Low', 'Close'])
df.head()
# print(df)