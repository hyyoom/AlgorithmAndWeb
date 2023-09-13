from django.shortcuts import render 
#템플릿을 이용해서 응답객체(html 포함) 생성


# Create your views here.
# 요청처리기
# 함수 모양이 결정되어 있음
'''
1. 첫번째 인자로 '요청'이라는 객체를 받아와야 함
2. 반환값으로 '응답' 객체를 반환함
render() : 템플릿을 이용해서 htaml 생성 및 응답 생성(그림 그리기)

템플릿: 알맹이(데이터) 빠진 html, 위치가 정해져있음. app/templates/하위에 작성해야함

ex) 홍길동님 반갑습니다. >> html
    {{name}}님 반갑습니다. >> 템플릿

렌더링 할때 필요한 데이터는 render함수의 인자로 넘겨줌
데이터는 딕셔너리 형태로 줌
'''

def hello(request): # hello라는 요청을 처리하는 함수 # 요청을 받음
    context={
        'name': request.GET.get('username'),
        'fruits':['apple','samsung','banana','kakao']
    }
    return render(request,'articles/hello.html',context) # 응답 반환(화면 그리기)

def name_form(request): #이름 입력 화면 응답함수
    return render(request,'articles/throw.html')