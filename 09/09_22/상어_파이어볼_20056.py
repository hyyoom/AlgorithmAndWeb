
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]


N,M,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N)]

for i in range(len(arr)):
    graph[arr[i][1]-1].append(arr[i][2:])

for i in range(len(graph)):
    for j in range(len(graph[i])):
        print(graph[i][j])


