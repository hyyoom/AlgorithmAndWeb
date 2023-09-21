# 마지막 연락 == v리스트에서 맥스값을 가진 애들 중 가잔 큰 인덱스 번호
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    v[start] = 1
    while q:
        p = q.popleft()
        for next in grap[p]:
            if not v[next]:
                v[next] = v[p]+1
                q.append(next)
    
# 2 7 11 6 6 6 2 15 15 4 4 2 4 10 7 1 1 7 1 8 1 17 3 22
for tc in range(1,11):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    v = [0] * (max(arr)+1)
    grap = [[] for _ in range(max(arr)+1)]
    for i in range(0,len(arr)-1,2):
        grap[arr[i]].append(arr[i+1])
    bfs(M)
    maxv = max(v)
    max_idx = -1
    ret = []
    for i in range(len(v)):
        if v[i] == maxv:
            ret.append(i)
    print(f"#{tc} {max(ret)}")