# hw_8_2.py

# 아래 함수를 수정하시오.

def check_number():
    
    while 1:
        try:
            N = int(input("숫자를 입력하세요 :"))
        except BaseException:
            print("잘못 된 입력입니다.",end="")
            break
        else:
            if N > 0:
                print("양수입니다.")
            elif N < 0:
                print("음수입니다.")
            else:
                print(f"{N}입니다.")
   

check_number()
