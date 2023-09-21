T = int(input())

def solve(v,idx,N,result):
    global minv
    if idx == N:
        if result < minv:
            minv = result
        return
    if result > minv:
        return
    for i in range(N):
        if not v[i]:
            v[i]=1
            solve(v,idx+1,N,result+arr[idx][i])
            v[i]=0
        

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    minv = 9999999
    solve(v,0,N,0)
    print(f"#{tc} {minv}")
    minv = 9999999