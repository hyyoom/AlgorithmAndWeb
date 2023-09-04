from collections import deque

T = int(input())
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x,v):
    q = deque()
    while water_dir:
        y,x = water_dir.pop()
        q.append([y,x])
        v[y][x] = 0
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<M and v[ny][nx] == -1 and maps[ny][nx] != "W":
                v[ny][nx] = v[y][x] + 1
                q.append([ny,nx])
    return 0


for tc in range(1, T+1):
    N,M = map(int,input().split())
    maps = [input().strip() for _ in range(N)]

    sums = 0
    water_dir = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'W':
                water_dir.append([i,j])
    v = [[-1]*M for _ in range(N)]
    bfs(i,j,v)

    for i in range(N):
        for j in range(M):
            if maps[i][j] == "L":
                sums += v[i][j]
    # for i in v:
    #     print(i)

    print(f"#{tc} {sums}")
        