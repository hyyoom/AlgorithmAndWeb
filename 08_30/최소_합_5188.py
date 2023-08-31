T = int(input())

def solve(i,j,total,result):
    if i >= N-1 and j >= N-1:
        total+=maps[N-1][N-1]
        result.append(total)
        return
    if i < N and j < N:
        solve(i+1, j,total+maps[i][j],result)
        solve(i, j+1,total+maps[i][j],result)

for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    result = []
    solve(0,0,0,result)
    # print(result)
    print(f"#{tc} {min(result)}")