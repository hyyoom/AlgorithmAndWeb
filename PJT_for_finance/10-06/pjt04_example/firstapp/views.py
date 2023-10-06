from django.shortcuts import render
import matplotlib.pyplot as plt

# io: 입출력 연산을 위한 PYTHON 표준 라이브러리
# bytesIO = 이진 데이터를 다루기 위한 버퍼를 제공
# 버퍼 = 임시 저장 공간
# 이진데이터로 임시로 저장하고 꺼내 쓰는 것
# 파일 시스템과 유사하지만, 실제로 파일로 만들지 않고, 메모리 단에서 작업할 수 있다.
from io import BytesIO
# 텍스트<->이진테이터 변환 모듈
import base64
# plt.show하면 백지 저장됨
# Create your views here.

plt.switch_backend('Agg')

def index(request):
    x = [1,2,3,4]
    y = [2,4,8,16]

    plt.clf()
    plt.plot(x, y)
    plt.title("TEST GRAPH")
    plt.ylabel("y~")
    plt.xlabel("x~")
    # 버퍼 생성
    buffer = BytesIO()
    # 버퍼에 그래프 저장
    plt.savefig(buffer, format="png")
    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    
    buffer.close()
    context = {
        'chart_image' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'index.html',context)

import pandas as pd
csv_path = 'firstapp/data/austin_weather.csv'


def example(request):
    df = pd.read_csv(csv_path)
    context = {
        'df' : df,
    }
    return render(request, 'example.html',context)