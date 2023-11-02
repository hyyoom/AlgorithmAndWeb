# 사과 == 1, 뱀 == 22
import sys
from collections import deque
input = sys.stdin.readline
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def solve():
    time = 0 #몇초 지났는지
    snake = deque()
    snake.append([0,0])
    d = 0 # 이동 위치
    y = 0
    x = 0
    maps[0][0] = 22
    while True:
        time+=1
        d = d%4
        ny = dirs[d][0] + y
        nx = dirs[d][1] + x
        y = ny
        x = nx
        if 0>ny or N<=ny or 0>nx or N<=nx or maps[ny][nx] == 22:
            # print(maps[ny][nx])
            # print(f'timesadfsd')
            return time
        if maps[ny][nx] == 1:
            maps[ny][nx] = 22 #늘리기
            snake.append([ny,nx])
        elif maps[ny][nx] != 1:
            maps[ny][nx] = 22 #늘리기
            snake.append([ny,nx]) #머리위치 추가
            tail = snake.popleft() #사과 없으니까 꼬리 줄이기
            maps[tail[0]][tail[1]] = 0 # 꼬리 부분 줄이기
        if dirs_time and dirs_time[0][0] == time:
            t, di = dirs_time.pop(0)
            if di == 'L':
                d -= 1
            elif di == 'D':
                d += 1
            d = d%4
            ny = dirs[d][0] + y
            nx = dirs[d][1] + x
        # print(f'시간 = {time} 방향 = {d} 방향 = {dirs[d]}')
        # for m in maps:
        #     print(m)
        # print()





N = int(input())
K = int(input())
maps = [[0]*N for _ in range(N)]
for _ in range(K):
    a,b = map(int,input().split())
    maps[a-1][b-1] = 1

L = int(input())
dirs_time = [list(input().split()) for _ in range(L)]
for dirs_t in dirs_time:
    dirs_t[0] = int(dirs_t[0])

print(solve())

# 5
# 3
# 1 0
# 1 1
# 1 2
# 5
# 0 D
# 1 L
# 3 D
# 4 D
# 5 D