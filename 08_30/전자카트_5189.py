def permutation(k,target,prev,amount):
    global answer
    if k == target:
        answer = min(answer, amount+maps[prev][0])
        return
    for i in range(1,N):
        if not v[i]:
            v[i] = 1
            permutation(k+1,target,i,amount+maps[prev][i])
            v[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * (N+1)
    answer = float('inf')
    permutation(0,N-1,0,0)
    print(f"#{tc} {answer}")
