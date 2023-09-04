from collections import deque

dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상,하,좌,우

pipe_next = { 
         0 : (1,2,5,6),
         1 : (1,2,4,7),
         2 : (1,3,4,5),
         3 : (1,3,6,7),
                        } 
# 내 지금 방향(dir)에서 다음 파이프가 될 수 있는 집합

# 파이프가 이동할 수 있는 방향
pipe_now_dir = { 
    1 : (0,1,2,3),
    2 : (0,1),
    3 : (2,3),
    4 : (0,3),
    5 : (1,3),
    6 : (1,2),
    7 : (0,2),
}

# 순서
# 첫 좌표에서 이동할 수 있는 방향으로 감. dir[pipe_now_dir[maps[i][j]], ny = ~
# pipe_next[maps[ny][nx]]에 maps[ny][nx]가 들어있다면 이동 가능함.
# 그렇게 time만큼 이동한 후 break

def bfs(y,x):
    v[y][x] = 1
    q = deque()
    q.append([y,x])
    while q:
        y,x = q.popleft()
        for next in pipe_now_dir[maps[y][x]]: #(0,1,2,3)
            ny = dir[next][0] + y #dir[0] = (-1,0)
            nx = dir[next][1] + x
            if 0<=ny<N and 0<=nx<M and not v[ny][nx]\
                and maps[ny][nx] in pipe_next[next]:
                v[ny][nx] = v[y][x]+1
                q.append([ny,nx])



T = int(input())
for tc in range(1,T+1):
    N,M,start_y, start_x,L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    v = [[0]*M for _ in range(N)]
    bfs(start_y,start_x)
    
    result = 0
    for i in range(N):
        for j in range(M):
            if v[i][j] <= L and v[i][j]:
                # print(v[i][j], end=" ")
                result+=1

    print(f"#{tc} {result}")
