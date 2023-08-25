import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
maps = [list(map(int, input().strip())) for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x):
    v = [[0]*M for _ in range(N)]
    q = deque([(y, x)])  # 수정된 부분: 좌표를 튜플 형태로 추가
    v[y][x] = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<M and not v[ny][nx] and maps[ny][nx] == 0:
                v[ny][nx] = v[y][x] + 1
                q.append((ny, nx))  # 수정된 부분: 좌표를 튜플 형태로 추가
    if v[N-1][M-1] == 0:
        return -1
    else:
        return v[N-1][M-1]


result = []
result.append(bfs(0,0))
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            maps[i][j] = 0
            result.append(bfs(0,0))
            maps[i][j] = 1

chk = 0
for i in result:
    if i == -1:
        chk += 1
if chk == len(result):
    print(-1)
else:
    print(max(result))