#1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

#인접행렬

V = 7
E = 8
adj = [[0] * (V+1) for _ in range(V+1)]
maps = [[] for _ in range(V+1)]

edges = list(map(int, input().split()))
for i in range(0, E*2, 2):
    adj[edges[i]][edges[i+1]] = 1
    adj[edges[i+1]][edges[i]] = 1
    maps[edges[i+1]].append(edges[i])
    maps[edges[i]].append(edges[i+1]) # maps[a].append(b)

def bfs_maps(start):
    visited = [0] * (V+1)
    visited[start] = 1
    queue = [start]
    while queue:
        # 정점에 방문해서 길찾기
        # 길찾으면 좀있다 방문할거니까 방문목록에 추가
        # 나머지길 계속 찾기
        front = queue.pop(0)
        print(front, end=" ") # 방문한 순서
        for i in maps[front]:
            if not visited[i]: # i번 노드가 현재 정점과 연결되어 있음
                visited[i] = 1
                queue.append(i)
    print()

def bfs(start):
    visited = [0] * (V+1)
    visited[start] = 1
    queue = [start]
    while queue:
        # 정점에 방문해서 길찾기
        # 길찾으면 좀있다 방문할거니까 방문목록에 추가
        # 나머지길 계속 찾기
        front = queue.pop(0)
        print(front, end=" ") # 방문한 순서
        for i in range(1, V+1):
            if adj[front][i] and not visited[i]: # i번 노드가 현재 정점과 연결되어 있음
                visited[i] = 1
                queue.append(i)
    print()

bfs(1)
bfs_maps(1)
