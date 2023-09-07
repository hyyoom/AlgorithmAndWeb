def f(i, N): # 현재값, 목표값
    if i == N: # 현재 == 목표
        return
    else:
        f(i+1,N)


N = 5
A = [1,2,3,4,5]
B = [0] * N

def f1(i, N): # 현재값, 목표값
    if i == N: # 현재 == 목표
        print(B)
        return
    else:
        B[i] = 1
        f1(i+1,N)
        B[i] = 0
        f1(i+1,N)
f1(0, N)
