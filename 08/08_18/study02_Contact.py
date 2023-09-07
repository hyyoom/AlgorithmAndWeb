'''
24 2
100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2
'''

def bfs(s,v):
    v[s] = 1
    q = [s]
    while q:
        nq = q.pop(0)
        for i in node[nq]:
            if not v[i]:
                v[i] = v[nq]+1
                q.append(i)


for tc in range(1, 11):
    E, S = map(int, input().split())
    node = [[] for _ in range(101)]
    v = [0] * 101

    edges = list(map(int, input().split()))

    for i in range(0, E, 2):
        node[edges[i]].append(edges[i+1])

    bfs(S,v)
    max_v = max(v)
    for i in range(len(v)-1,-1,-1):
        if max_v == v[i]:
            print(f"#{tc} {i}")
            break