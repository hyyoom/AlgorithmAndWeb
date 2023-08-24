T = int(input())

def bfs(s,g):
    q = [s]
    visit[s] = 1

    while q:
        next_q = q.pop(0)
        if next_q == g:
            return visit[next_q]-1
        for i in node[next_q]:
            if visit[i] == 0:
                visit[i] = visit[next_q] + 1
                q.append(i)
    return 0


for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]
    
    for _ in range(E):
        a,b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    S,G = map(int, input().split())

    print(node)
    print(S,G)

    visit = [0] * (V+1)

    # ret = bfs(S,G)
    # if ret == 0:
        # print(f"#{tc} {ret}")

    print(f"#{tc} {bfs(S,G)}")