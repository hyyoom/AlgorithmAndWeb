# dijkstra 알고리즘
# 시작 정점에서 각 정점까지 최소비용 계산
# 1. 시작 정점에서 각 정점까지 갈 수 있는 비용 계산 
#   만약 인접하지 않았다면, 비용은 매우크게
# 2. 비용이 가장 적게 드는 정점 선택, 
# 3. 정점을 선택했으니, 그 정점을 거쳐서 다른 정점으로 갔을 때 비용을 계산
#    만약 그 비용이 알고 있는 비용보다 더 작다면, 비용 수정
# 4. 모든 정점까지 비용을 계산할 때 까지 반복

V,E = map(int, input().split())
graph = [0xfffff] * V

for _ in range(E):
    s, e, w = map(input().split())
    graph[s][e] = w


def dijkstra(start):
    # 시작 정점에서 각 정점으로 가는 비용을 담은 배열
    weight = graph[start][:]
    
    # 정점까지 가는 비용이 확정된 정점의 목록
    selected = set()
    
    weight[start] = 0 # 시작 정점에서 시작 정점까지 가는 비용은 0
    
    # 모든 정점에 대해서 비용을 확정할 때 까지 반복
    while len(selected) < V:
        # 아직 비용이 확정되지 않았고, 비용이 가장 적게 드는 정점을 선택
        min_weight = 0xfffff
        min_node = None
        for i in range(len(V)):
            if i not in selected and weight[i] < min_weight:
                min_node = i
                min_weight = weight[i]
        selected.add(min_node)
        # min_node를 통해서 갈 수 있는 새로운 경로에 대한 비용 계산
        # min_node까지 가는 비용+min_node에서 다른 노드로 가는 비용

        for i in range(V):
            # 원래 알던거 vs min_node거쳐서 가는 비용
            # weight[i] vs min_weight + graph[min_node][i]