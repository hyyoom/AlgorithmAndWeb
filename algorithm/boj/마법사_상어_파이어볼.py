N, M, K = map(int,input().split())

direct = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
maps = [[0]*N for _ in range(N)]

fire_ball = [list(map(int,input().split())) for _ in range(M)]


for _ in range(K):
    for i in range(len(fire_ball)):
        r,c,m,s,d = fire_ball[i]
        s_tmp = s
        while s_tmp: # 파이어볼 보내기
            r = r + direct[d][0]
            c = c + direct[d][1]
            if r == N:
                r = 0
            elif r == -1:
                r = N-1
            if c == N:
                c = 0
            elif c == -1:
                c = N-1
            s_tmp -= 1
        fire_ball[i][0] = r
        fire_ball[i][1] = c
    fire_ball = sorted(fire_ball, key=lambda x:(x[0],x[1]))

    # 이제 합치기
    i = len(fire_ball)-1
    while i > 0:
        cnt = 1
        r,c,d,r1,c2 = fire_ball[i][0],fire_ball[i][1],fire_ball[i][4],fire_ball[i-1][0],fire_ball[i-1][1]
        if r == r1 and c == c2:
            cnt += 1 # 합쳐진 파이어볼 갯수
            z,x,m,s,d2 = fire_ball.pop(i)
            fire_ball[i-1][2] += m
            fire_ball[i-1][3] += s+999999
            if d%2 != d2%2 and fire_ball[i-1][4] != -1: #틀렸던 적이 있다면 -1로 바꿀거임
                fire_ball[i-1][4] = -1
            if fire_ball[i-1][4] == -1:
                fire_ball[i-1][4] = -1
            i-=1
            maps[r][c] = cnt
        else:
            cnt = 1
        i-=1
    for m in maps:
        print(m)
    print(fire_ball)
    tmp = []
    i = len(fire_ball)-1
    while i>=0:
        if fire_ball[i][3] > 999999:
            fire_ball[i][3] -= 999999
            r,c,m,s,d = fire_ball.pop(i)
            new_m = m//5
            if new_m == 0:
                continue
            new_s = s//maps[r][c]
            if d == -1:
                tmp2 = [1,3,5,7]
            else:
                tmp2 = [0,2,4,6]
            for t in tmp2:
                tmp.append([r,c,new_m,new_s,t])
        i-=1
    fire_ball += tmp
# print(fire_ball)












    # 나누기(소멸시키기)


