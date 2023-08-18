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
print(maps, change_dir)

for i in maps:
    print(i)