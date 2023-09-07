dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x):
    v = [[0] * 100 for _ in range(100)]
    q = [(y,x)]
    v[y][x] = 1

    while q:
        y, x = q.pop(0)
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<100 and 0<=nx<100:
                if maps[ny][nx] == 2:
                    return 1
                if maps[ny][nx] == 0 and v[ny][nx] == 0:
                    v[ny][nx] = 1
                    q.append((ny,nx))
    return 0

for tc in range(1, 11):
    T = int(input())
    maps = [list(map(int, input().strip())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if maps[i][j] == 3:
                ret = bfs(i,j)
    print(f"#{tc} {ret}")

