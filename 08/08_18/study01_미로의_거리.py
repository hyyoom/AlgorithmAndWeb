T = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x):
    q = [(y,x)]
    v[y][x] = 1
    while q:
        y,x = q.pop(0)
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<N:
                if maps[ny][nx] == 3:
                    return v[y][x]
                if maps[ny][nx] == 0 and v[ny][nx] == 0:
                    v[ny][nx] = v[y][x] + 1
                    q.append((ny,nx))


for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().strip())) for _ in range(N)]
    v = [[0] * (N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 2:
                ret = bfs(i,j)
    if ret != None:
        print(f"#{tc} {ret-1}")
    else:
        print(f"#{tc} 0")