# 부분조합 중복없이 만들기
# 만든 조합과 결합,,,,,,,,,,,,,

T = int(input())
for tc in range(1,T+1):
    flag = 0
    Num = float(input())
    len_N = len(str(Num))-2
    
    # 부분집합 만드는 재귀
    def f(i, N, s): # s = i-1단계까지의 부분집합의 합(포함된 원소의 합)
        global flag
        if i == N:
            if s == Num:
                flag = 1
                print(f"#{tc}",end=" ")
                for i in bit:
                    print(i,end="")
                print()
            return
        else:
            bit[i] = 1 # 부분집합에 A[i] 포함
            f(i+1, N, s+(1/two[i]))
            bit[i] = 0
            f(i+1, N, s) # 미포함

    two = []
    tmp = 1
    for i in range(1, 14):
        tmp = tmp*2
        two.append(tmp)

    bit = [0] * len_N
    f(0,len_N,0)

    if flag == 0:
        print(f"#{tc} overflow")