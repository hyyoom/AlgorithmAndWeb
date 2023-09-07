
# 부분집합 만드는 재귀
cnt = 0
def f(i, N, s, t): # s = i-1단계까지의 부분집합의 합(포함된 원소의 합)
    # t == target 찾으려는 합
    global cnt
    cnt += 1
    if s == t:
        print(bit)
        return 
    elif i == N: # t는 아니지만 남은 원소가 없는경우
        return
    elif s > t:
        return
    else:
        bit[i] = 1 # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i],t)
        bit[i] = 0
        f(i+1, N, s,t) # 미포함

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
N = 10
t = 10
s = 0
A = [i for i in range(1, N+1)]
bit = [0] * N
f(0, N, s, t) # 55를 넣으면 cnt == 2047, 즉 백트래킹을 해도 최악의 경우엔 그냥 재귀와 동일하다.
print(cnt)