# 예외 처리하기

try:
    n = int(input("100으로 나눌 값을 입력하세요"))
except ValueError:
    print("아니 숫자 하라고 성모야;;;;")
except ZeroDivisionError:
    print("0으로 뭘 나누냐;;")