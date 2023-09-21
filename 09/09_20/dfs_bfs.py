# 인접행렬
# 장점 : 구현이 쉽다
# 단점 : 메모리 낭비 (0도 표시해서)
# if arr[0][1] == 1:
#    갈수있다.

arr = [
    [0,1,0,1,0],
    [1,0,1,1,1],
    [0,1,0,0,0],
    [1,1,0,0,1],
    [0,1,0,1,0],
]
# DFS
# stack버전
def dfs_stack(start):
    v = []
    stack = [start]
    while stack:
        now = stack.pop()
        if now in v:
            continue
        v.append(now)
        for next in range(5):
            if arr[now][next] == 1 and next not in v:
                stack.append(next)
    return v

print(dfs_stack(0))

graph = [[1,3],[0,2,3,4],[1],[0,1,4],[1,3]]

v = [0] * 5
def dfs(now):
    v[now] = 1

    for next in graph[now]:
        if graph[next] == []:
            continue
        if v[next]:
            continue
        print(next)
        dfs(next)
print(dfs)
# 재귀 버전