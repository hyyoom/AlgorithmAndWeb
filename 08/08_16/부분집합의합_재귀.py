
# 부분집합 만드는 재귀
def f(i, N):
    if i == N:
        s = 0
        for j in range(N):
            if bit[j] == 1:
                s += A[j]
                # print(A[j], end=" ")
        print(s)
        # print()
        return
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = [1,2,3]
bit = [0] * 3
f(0, 3)