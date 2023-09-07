T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    q = list(map(int, input().split()))

    while M:
        tmp = q.pop(0)
        q.append(tmp)
        M-=1
    print(f"#{tc} {q[0]}")