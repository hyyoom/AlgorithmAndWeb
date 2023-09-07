T = int(input())


dy = [-1,1,0,0]
dx = [0,0,-1,1]


# while stack 활용
def solve2(y,x):
    v = [[0] * N for _ in range(N)]
    st = [(y,x)]
    v[y][x] = 1
    while st:
        y, x = st.pop()
        if maze[y][x] == "3":
            return 1
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<nx<N and \
                maze[ny][nx] != "1" and not v[ny][nx]:
                v[ny][nx] = 1
                st.append((ny,nx))
    return 0
        

def dfs(y,x):
    if maze[y][x] == "3":
        return 1
    visited[y][x] = 1
    for d in range(4):
        ny = dy[d] + y
        nx = dx[d] + x
        # 0이 통로
        if 0<=ny<N and 0<nx<N and \
            maze[ny][nx] != "1" and not visited[ny][nx]:
            visited[ny][nx] = 1
            if dfs(ny,nx) == 1:
                return 1
    return 0


for tc in range(1, T+1):
    N = int(input())
    maze = [input().strip() for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ret = 0
    ret2 = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                ret = dfs(i,j)
                ret2 = solve2(i,j)
                break
    print(ret, ret2)
    