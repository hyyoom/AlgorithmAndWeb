T = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]
ret = []

def dfs(y,x,v,step,flag):
    global ret
    if 0>y or N<=y or 0>x or N<=x:
        return
    # for k in range(N):
    #     print(v[k])
    # print(f"======{step}=====")
    # print()
    if maps[y][x] == 0:
        return
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0<=ny<N and 0<=nx<N and maps[ny][nx] < maps[y][x] and not v[ny][nx]:
            v[ny][nx] = v[y][x]+1
            step += 1
            dfs(ny,nx,v,step,flag)
            step -= 1
            v[ny][nx] = 0

        elif 0<=ny<N and 0<=nx<N and maps[ny][nx] >= maps[y][x] and not v[ny][nx] and flag == 0:
            if maps[ny][nx] - K < maps[y][x]:
                v[ny][nx] = v[y][x]+1
                step += 1
                flag = 1
                maps[ny][nx] -= 1
                dfs(ny,nx,v,step,flag)
                maps[ny][nx] += 1
                v[ny][nx] = 0
                step -= 1
                flag = 0
    ret.append(step)
    # v[y][x] = 0

for tc in range(1,T+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    maps_max_v = max(map(max, maps))
    start_point = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == maps_max_v:
                start_point.append((i,j))
    v = [[0]*N for _ in range(N)]
    ret = []
    for start in start_point:
        dfs(start[0],start[1],v,0,0)

    print(f'#{tc} {max(ret)+1}')
    # print(ret)
    
