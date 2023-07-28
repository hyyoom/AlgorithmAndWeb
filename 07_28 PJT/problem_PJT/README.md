1. problem_A

  해당 과제는 그닥 어려운게 없었고,  csv(데이터)를 불러올때 정해진 포맷이 있고, 경로를 설정 해 주어야 한다는 것을 배웠다


2. problem_B

  df가 데이터 프레임이라는 것을 배웠다.. pandas에도 당연히 데이터타입이 존재 할 텐데 그 부분을 인지하지 못해서 뭐가 뭔지를 잘 몰랏다.. datetime도 하나의 자료형 인것 같은데(클래쓰?)잘 이해는 되지 않아서 어려웠다


3. problem_C

  B문제에서 달라진것은 없고 데이터.max() 를 사용해 보는 문제였다.


3. problem_D

  여기서부터 데이터 필터링을 하는 방식을 조금 알겠어서, df["date"] = pd.to_datetime(df["date"])를 통해 dt로 자료형을 변환시켜줬다.(객체?..)
  그 후 avg_data에 data frame 밑에 date time 밑의 to_period를 사용하는데 freq값을 M으로 주고 mean을 사용하여 평균을 냈다. 그리고 그것을 그룹핑 하였다.
  그 후엔 plt.plot(avg_data['Date'],avg_data['Close'])를 통해 x,y축을 정하여 그래프를 생성하였다


4. problem_E
   데이트 타임을 22년 후부터로 지정해서 filter_data에 저장한 후, filter_data의 date를 x축 y축은 각자 high, low, close로 설정하고 label에 각 이름을 입력하였다.
   그 후 plt.legend()를 사용하여 범례를 표기하였다.

