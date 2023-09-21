from collections import deque
T = int(input())

op = [1,1,2,-10]

def bfs(start):
    q = deque()
    q.append(start)
    v[start] = 1

    while q:
        x = q.popleft()
        if x == M:
            return v[x]
        for i in range(4):
            if i == 0:
                nx = x+1
            elif i == 1:
                nx = x-1
            elif i == 2:
                nx = x*2
            else:
                nx = x-10
            if nx > 1000000:
                continue
            if not v[nx]:
                v[nx] = v[x] + 1
                q.append(nx)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    v=[0] * 2000001
    ret = bfs(N)
    print(f"#{tc} {ret-1}")