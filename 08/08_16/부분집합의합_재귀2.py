
# 부분집합 만드는 재귀
def f(i, N, s): # s = i-1단계까지의 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(bit, end=" ")
        print(f": {s}")
        return
    else:
        bit[i] = 1 # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i])
        bit[i] = 0
        f(i+1, N, s) # 미포함

A = [1,2,3]
bit = [0] * 3
f(0, 3, 0)