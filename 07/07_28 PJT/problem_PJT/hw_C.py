import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = 'data/NFLX.csv'
df = pd.read_csv(csv_path, usecols=range(0, 5))
df.head()
df_after_2022 = df[df["Date"] >= "2021-01-01"]
pd.to_datetime(df_after_2022["Date"]), df_after_2022['Close']


print("최고 종가:",df_after_2022["Close"].max())
print("최고 종가:",df_after_2022["Close"].min())