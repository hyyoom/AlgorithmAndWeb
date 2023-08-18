from collections import deque
import sys
input = sys.stdin.readline

dir = [(0,1), (1,0), (0,-1), (-1,0)]

N = int(input())

maps = [[0] * N for _ in range(N)]
apple_N = int(input())
apple_direction = [map(int,input().split()) for _ in range(apple_N)]

for i, j in apple_direction:
    maps[i][j] = 2

change_dir_N = int(input())
change_dir = [list(input().split()) for _ in range(change_dir_N)]

for i in change_dir:
    i[0] = int(i[0])
maps[0][0] = 1
def bfs():
    dir_i = 0
    snake = deque()
    snake.append([0,0])
    time = 0
    while snake:
        y,x = snake.popleft()
        ny = dir[dir_i][0] + y
        nx = dir[dir_i][1] + x
        if 0<=ny<N and 0<=nx<N:
            if maps[ny][nx] == 1:
                return time
            snake.append([ny,nx])        
            if maps[ny][nx] == 2:
                maps[ny][nx] = 1
                maps[y][x] = 1
            else:
                maps[ny][nx] = 1
                maps[y][x] = 0
        else:
            return time
        for i in change_dir:
            if time in i:
                if i[1] == "D":
                    dir_i = (dir_i + 1) % 4
                elif i[1] == "L":
                    dir_i = (dir_i - 1) % 4
        for i in maps:
            print(i)
        print()
        time+=1
    return time
                
print(bfs())
for i in maps:
    print(i)























