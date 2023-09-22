import math


def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    p[find_set(x)] = find_set(y)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    distance = list(zip(x, y))
    rate = float(input())
    
    # nodes = [[] for _ in range(N+1)]
    nodes = []
    for i in range(N):
        for j in range(i+1, N):
            nodes.append((i,j,math.sqrt(abs(distance[i][0] - distance[j][0])**2 + abs(distance[i][1] - distance[j][1])**2)))
    p = [i for i in range(N)]

    nodes.sort(key=lambda x:x[2])


    ret = []
    cnt = 0
    for node in nodes:
        s,e,w = node
        if find_set(s) != find_set(e):
            union(s,e)
            ret.append(w)
    ans = 0
    for r in ret:
        tmp = (r**2)
        ans+=rate*tmp
    print(f"#{tc} {round(ans)}")

