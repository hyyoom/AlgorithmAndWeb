# 예외 처리하기

try:
    n = int(input("100으로 나눌 값을 입력하세요\n"))
    print(100 / n)
except ValueError: 
    # 밑에 있는 에러의 상위 클래스 이기에 밑으로 내려가지 못함
    # 하위 클래스부터 써야함
    print("아니 숫자 하라고 성모야;;;;")
except ZeroDivisionError:
    print("0으로 뭘 나누냐;;")
except:
    print("ㅈㅅㅈㅅ;;")