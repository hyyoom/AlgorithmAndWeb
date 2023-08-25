T = int(input())

def solve(idx_i, idx_j, k, spend):
    cnt = 0
    for i in range(N):
        for j in range(N):
            tmp_i = abs(idx_i - i)
            tmp_j = abs(idx_j - j)
            if tmp_i + tmp_j <= k - 1 and city[i][j] == 1:
                cnt += 1

    benefit = (cnt * M) - spend

    if benefit >= 0:
        return(cnt)

    return 0

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    ret = []
    for i in range(N):
        for j in range(N):
            for k in range(0, N+1):
                spend = (k * k) + (k - 1) * (k - 1)
                chk = solve(i, j, k, spend)
                ret.append(chk)
    # print(ret)
    one = 0
    check = 0
    for i in range(N):
        for j in range(N):
            check += 1
            if city[i][j] == 1:
                one+=1
    if check == one:
        print(f"#{tc} {max(ret)+1}")
    else:
        print(f"#{tc} {max(ret)}")
