import copy

min_cnt = 9999999
flag = 1

def problem(result,re_cnt):
    global flag
    global min_cnt # 성공시 쓴 필터갯수로 바꿔 실패시 min_cnt= 999999

    tmp_maps = [[0]*W for _ in range(D)]

    for i in range(D):
        for j in range(W):
            if result[i] == 2:
                tmp_maps[i][j] = maps[i][j]
            else:
                tmp_maps[i][j] = result[i]

    find = 0
    for j in range(W):
        cnt = 1
        for i in range(D-1):
            if K == cnt:
                find += 1
                cnt = 1
                break
            if tmp_maps[i][j] == tmp_maps[i+1][j]:
                cnt += 1
            else:
                cnt = 1

    if find == W:
        return re_cnt
    else:
        return min_cnt
        # for i in tmp_maps:
            # print(i)
        # print()
        # print(result)
    
    # if result == [2,2,0,2,2,1]:
    #     print(result)
    #     for i in tmp_maps:
    #         print(i)
    #     print()

def solve(idx,N,result):
    global min_cnt
    if idx == N:
        cnt = 0
        for re in result:
            if re == 1 or re == 0:
                cnt += 1
        # if min_cnt >= cnt:
        chk = problem(result,cnt)
        if min_cnt > chk:
            print(chk)

            # problem(result,cnt)
        return
    for i in range(3):
        solve(idx+1,N,result+[arr[idx][i]])


T = int(input())
for tc in range(1, T+1):
    D,W,K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(D)]

    arr = [[0,1,2] for _ in range(D)]
    v = [0] * 3
    solve(0,D,[])
    print(min_cnt)
    min_cnt = 9999999
    flag = 1