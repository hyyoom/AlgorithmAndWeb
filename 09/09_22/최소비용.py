'''
prim, krwskal = 모두 연결한다 시작점 끝점 없음
dijkstra 시작, 목적지 있음, 최단거리, 최소비용



'''


def dijkstra(sr, sc):
    #시작 정점에서 각 정점까지 가는 비용을 저장
    #그 비용 중에서 제일 작은애를 골라서 비용 확정
    weights = [[0xfffffff] * N for _ in range(N)]
    weights[sr][sc] = 0
    # 모든 비용중에 제일 작은 비용 고르기

    checked = set()
    # 비용 확정된 애들은 고르지 않음
    while True:
        minv = 0xfffff
        min_r, min_c = -1, -1
        for i in range(N):
            for j in range(N):
                if (i,j) not in checked and weights[i][j] < minv:
                    minv = weights[i][j]
                    min_r, min_c = i, j

        # 경로 최소비용이 확인된 정점을 추가
        checked.add((min_r,min_c))
        # 새로운 정점이 추가 되었으니 경로도 새로 생겼을 것
        # 새롭게 추가된 정점으 ㅣ인접한 정점으로 가는 경로 비용 계산
        if (min_r, min_c) == (N-1,N-1):
            break
        for d in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc =  min_r+d[0], min_c+d[1]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 경로 비용 계산인데 이동비용1, 높이 차이비용
            # 이동 하려는 곳의 높이가 더 높다면 오른쪽 음수면 왼쪽 0 선택
            new_cost = 1 + max(0,maps[nr][nc] - maps[min_r][min_c])
            # 원래 알고있던 비용이랑 비교해서 새로 계산한 비용이 더 작으면 바꿔주기
            # 원래 알던 비용 weights[nr][nc]
            if weights[nr][nc] >  new_cost + weights[min_r][min_c]:
                weights[nr][nc] = new_cost + weights[min_r][min_c]
    return weights[N-1][N-1]
        


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {dijkstra(0,0)}")