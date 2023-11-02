import heapq
import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]
ret = []
def dijkstra(tc):
    q = []
    global ret
    weight = [[0xfffff]*N for _ in range(N)]
    heapq.heappush(q,(maps[0][0],0,0))
    weight[0][0] = 0
    while q:
        w, y, x = heapq.heappop(q)
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<N:
                new_w = w + maps[ny][nx]
                if new_w < weight[ny][nx]:
                    weight[ny][nx] = new_w
                    for k in maps:
                        print(k)
                    print()
                    for k in weight:
                        print(k)
                    print("------------------")
                    heapq.heappush(q,(new_w, ny,nx))
    ret.append(weight[N-1][N-1])

while True:
    tc = 1
    N = int(input())
    if not N:
        break
    maps = [list(map(int, input().split())) for _ in range(N)]
    dijkstra(tc)
    # print(ret)

for re in ret:
    print(f'Problem {tc}: {re}')
    tc+=1