
def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    p[find_set(x)] = find_set(y)


T = int(input())
for tc in range(1, T+1):
    V,E = map(int, input().split())
    node = [[] for _ in range(V)]
    for _ in range(E):
        a,b = map(int, input().split())
        node[a].append(b)
    p = [x for x in range(V)]
    
    