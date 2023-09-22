import sys
input = sys.stdin.readline

from heapq import heappop, heappush
# f to w

def dstra(start): #시작점, 끝점
    weights[start] = 0
    q = []
    heappush(q,(0, start))

    while q:
        w, p = heappop(q)
        for next in nodes[p]:
            nw,np = next
            new_weight = w+nw
            if new_weight < weights[np]:
                weights[np] = new_weight
                heappush(q, (new_weight, np))

V,E = map(int, input().split())
start = int(input())
nodes = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    nodes[a].append((w,b))

weights = [0xfffff] * (V+1)
dstra(start)

for i in range(1, V+1):
    if weights[i] == 0xfffff:
        print("INF")
    else:
        print(weights[i])