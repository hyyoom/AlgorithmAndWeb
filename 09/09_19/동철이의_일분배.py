T = int(input())


def solve(v,idx,N,result):
    global minv
    if result == 0:
        return
    if idx == N:
        if minv < result:
            minv = result
        return
    if minv > result:
        return
    for i in range(N):
        if arr[idx][i] == 0:
            continue
        if not v[i]:
            v[i] = 1
            solve(v,idx+1,N,result*(arr[idx][i] / 100))
            v[i] = 0


for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    minv = -9999
    solve(v,0,N,1)
    print(f"#{tc} {minv*100:.6f}")
    minv = -9999