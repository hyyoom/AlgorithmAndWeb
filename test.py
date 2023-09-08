from collections import deque

T = int(input())
dx = [1,-1,2,-10]


def bfs(N,M):
    q = deque()
    q.append(N)
    v = [0] * (M+1)
    v[N] = 1
    while q:
        x = q.popleft()
        for i in range(4):
            if i == 2:
                nx = x*2
            else:
                nx = x+dx[i]
            if 0<=nx<=M and not v[nx]:
                v[nx] = v[x]+1
                print(nx)
                q.append(nx)
    print(v)


for tc in range(1, T+1):
    N ,M = map(int, input().split())
    tmp = bfs(N,M)
    
