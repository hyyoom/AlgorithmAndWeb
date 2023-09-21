import sys
sys.setrecursionlimit(10**5)

dy = [-1,1,0,0,-1,-1,1,1]
dx = [0,0,-1,1,-1,1,-1,1]

def bfs(i,j):
    v[i][j] = 1
    for k in range(8):
        ny = dy[k] + i
        nx = dx[k] + j
        if 0<=ny<N and 0<=nx<M:
            if not v[ny][nx] and grap[ny][nx] == 1:
                v[ny][nx] = 1
                bfs(ny,nx)

while True:
    M,N = map(int, input().split())
    if not M and not N:
        break
    grap = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not v[i][j] and grap[i][j]:
                cnt += 1
                v[i][j] = 1
                bfs(i,j)

    print(cnt)



