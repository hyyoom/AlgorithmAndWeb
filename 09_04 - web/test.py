from collections import deque

dy = [-1,1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]


M,N,H = map(int,input().split())

maps = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
v = [[[0]*M for _ in range(N)] for _ in range(H)]

chk = M*N*H
ret = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if maps[h][i][j] == 1 or maps[h][i][j] == -1:
                ret += 1
if chk == ret:
    print(0)
    exit()



def bfs():
    q = deque()
    for to in tomato:
        q.append(to)
        v[to[0]][to[1]][to[2]] = 1
    
    while q:
        h,y,x = q.popleft()
        for i in range(6):
            ny = dy[i]+y
            nx = dx[i]+x
            nh = dh[i]+h
            if 0<=ny<N and 0<=nx<M and 0<=nh<H:
                if not v[nh][ny][nx] and not maps[nh][ny][nx]:
                    v[nh][ny][nx]=v[h][y][x]+1
                    q.append([nh,ny,nx])
            

tomato = []
for h in range(H):
    for i in range(N):
        for j in range(M):
            if maps[h][i][j] == 1:
                tomato.append([h,i,j])
            if maps[h][i][j] == -1:
                v[h][i][j] = -1
                

bfs()
ret = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if ret < v[h][i][j]:
                ret = v[h][i][j]
            if v[h][i][j] == 0:
                ret = -1
                print(-1)
                exit()


print(ret-1)