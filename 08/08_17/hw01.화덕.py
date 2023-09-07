T = int (input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    for i in range(len(cheese)):
        cheese[i] = (cheese[i], i+1)

    oven = cheese[:N]
    cnt = 0

    while True:
        if len(oven) == 1:
            break
        tmp = oven.pop(0)

        if (tmp[0] // 2) == 0:
            if N+cnt < M:
                oven.append(cheese[N+cnt])
                cnt += 1
        else:
            tmp1 = tmp[0]//2
            tmp2 = tmp[1]
            tmp = (tmp1, tmp2)
            oven.append(tmp)
    print(f"#{tc} {oven[0][1]}")

