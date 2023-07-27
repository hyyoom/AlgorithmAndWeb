# 예외 처리하기

try:
    n = int(input("100으로 나눌 값을 입력하세요\n"))
    print(100 / n)
except BaseException: 
    # 밑으로 내려가지 않음. BaseException 에러처리 계층구조를 보고 밑의 계층부터 확인하며 처리해야함!
    print("아니 숫자 하라고 성모야;;;;")
except ZeroDivisionError:
    print("0으로 뭘 나누냐;;")
except:
    print("ㅈㅅㅈㅅ;;")