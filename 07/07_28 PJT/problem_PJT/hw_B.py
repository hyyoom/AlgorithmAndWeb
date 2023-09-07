import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = 'data/NFLX.csv'
df = pd.read_csv(csv_path, usecols=range(0, 5))
df.head()
df_after_2022 = df[df["Date"] >= "2021-01-01"]
# df_after_2022["Date"] = pd.to_datetime(df_after_2022["Date"])

# 그래프 그리기 (가로, 세로 축에 표시될 데이터를 차례로 기입)
plt.plot(pd.to_datetime(df_after_2022["Date"]), df_after_2022['Close'])

# 그래프 제목 설정
plt.title('Close Prices over Time')

# x축 레이블 설정
plt.xlabel('Date')
plt.xticks(rotation=45)
# y축 레이블 설정
plt.ylabel('Close')

# 그래프 표시
plt.show()