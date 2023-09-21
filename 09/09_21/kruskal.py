# kruskal 알고리즘
# 최소 신장트리 구하기 - MST
# 모든 정점을 최소 비용으로 연결하기
# MST를 만드는 과정
# 1. 간선을 가중치 기준으로 오름차순 정렬
# 2. 간선을 작은 순으로 선택해간다
#    단, 선택했을 때 사이클이 생긴다면 선택하지 않음
# 3. 위 과정을 모든 정점이 MST에 포함될 때 까지 반복
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

V, E = map(int,input().split())
graph = []
for _ in range(E):
    graph.append(tuple(map(int,input().split())))

# 가중치 기준으로 오름차순 정렬
graph.sort(key=lambda x: (x[2]))
MST = []
p = [x for x in range(V)]

def find_set(x):
    if x == p[x]:
        return x
    
    p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    p[find_set(x)] = find_set(y)
    



while len(MST) < V-1: # MST는 간선 비용 이라서 간선은 정점 - 1 임
    s,e,w = graph.pop(0)
    # s랑 e를 추가했을때 싸이클이 발생하지 않으면
    # 사이클 검사 -> 서로소 집합 활용
    # 이미 MST에 들어있는 두 정점을 추가하면 사이클이 생긴다.
    if find_set(s) != find_set(e):
        MST.append((w,s,e))
        union(s,e)

print(MST)