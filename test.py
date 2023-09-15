T = int(input())
minv = 99999999
maxv = -99999999
 

def solve(idx,N,result,nums,ret):
    if idx == N-1:
        return
    for i in range(N):
        solve(idx+1,N,result+)

              
for tc in range(1, T+1):
    N = int(input())
    op = list(map(int,input().split()))     
    nums=list(map(int, input().split()))
    # print(nums)
     
    v = [0]*len(op)
    ret = []
    solve(0,N,0,nums,ret)
    print(f"#{tc} {maxv-minv}")
    maxv = -99999999
    minv = 99999999