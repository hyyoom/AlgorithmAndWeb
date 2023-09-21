T = int(input())

def solve(idx,result,cnt):
    global minv
    if idx == N:
        if minv > result:
            minv = cnt
        return
    if result >= N:
        if minv > result:
            minv = cnt
        return
    for i in range(1,arr[idx]+1):
        solve(idx,result+arr[idx],cnt+1)
    # solve(v,idx+2,N,result+arr[idx+2],cnt+1)

for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    minv = 999999
    v = [0]*(N-2)
    solve(0,0,0)
    print(f"#{tc} {minv}")
    minv = 999999