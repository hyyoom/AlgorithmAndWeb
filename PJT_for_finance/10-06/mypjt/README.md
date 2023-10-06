problem 1

- pandas를 이용하여 csv를 읽어와 웹에 게시하는 문제여서 그리 어렵지 않았습니다.
- 하지만, csv를 읽어와 templates에서 표현하는 방법이 이해가 조금 어려웠습니다.

problem 2

- pandas를 써본지 너무 오래되어 사용방법을 모두 잊어버렸기에 어려웠습니다,.
- 각변수에 읽어온 dataframe에서 필요 부분을 뽑아 저장하고 표로 표현합니다.
- 이때 6개월 단위로 표현하기 위해서 
    ax = plt.gca()
    ax.xaxis.set_major_locator(dates.MonthLocator(interval=6))
    를 사용하였습니다.


problem 3

- dataframe에서 dataframe[['Date','TempHighF','TempAvgF','TempLowF']]같이 필요한 변수만 뽑아와 Date의 경우 datetime형식으로 나머지는 numeric형식으로 변환합니다.
- 그 후 groupby를 통하여 월별로 묶어 평균값을 구합니다.
- groupby는 새로운 데이터를 반환하므로 그 데이터에서 각 필요 데이터를 뽑아 
- 각 필요 데이터마다 plt.plot을 통해 웹상에 게시합니다.
- plt.legend()로 범례를 표시합니다


problem 4

- 필요한 Events만 뽑아와서 df변수에 저장합니다.
- 그후 딕셔너리를 통하여 띄어쓰기가 하나만 들어있는 Events는 weathers['No Events']에 값을 저장해주고
- 나머지는 두개 이상일 경우를 대비하여 split을 통해 나누어 weathers 딕셔너리에 저장합니다.
- 그 후 plt.bar로 히스토그램을 작성합니다.