# tmp = [
#     [1,2,3,1],
#     [2,1,3,2],
#     [1,3,3,3],
#     [4,1,3,4],
#     [1,3,3,5]
# ]

# tmp = sorted(tmp, key=lambda x:(x[0],x[1],x[2]))
# print(tmp)
# tmp = [0,1,2,3,4,5]
# print(tmp[8%6])
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

# 행과 열은 1~N이 연결되어있다. 
# 즉, N을 넘어가면 %N 하면 될듯..

# 모든 파이어볼은 자신의 방향으로 속력만큼 이동
# 한번에 해야하니 반복문으로 처리

#이동이 끝난뒤 2개 이상의 파이어볼이 있는 칸을 찾는다
#같은 칸에 있는 파이어볼 모두 합쳐짐
#4개로 나뉘어짐
#질량 = 파이어볼 질량합/5
#속력 = 파이어볼 속력합/합쳐진 파이어볼 갯수, 합쳐진거 다른거 아님! 
#여기서 확인할 것, 만약 합쳐진 속력이 N을 넘으면 질량%N해주기
#방향 = 합쳐지는 파이어볼의 방향이 모두 같다면, 0,2,4,6 아니면 0,3,5,7
#질량이 인 파이어볼은 없어짐
#K번 이동 명령 후 남아있는 파이어볼 질량의 합!


#1. 입력
N,M,K = map(int,input().split())
fire_ball = [list(map(int, input().split())) for _ in range(M)]

for i in range(len(fire_ball)):
    fire_ball[i].append(0)
    fire_ball[i].append(0)
    fire_ball[i].append(0)
    fire_ball[i].append(1)


for _ in range(K):
    for i in range(len(fire_ball)):
        fire_ball[i][5] = 0
        fire_ball[i][6] = 0
        fire_ball[i][7] = 0
        fire_ball[i][8] = 1
    # 속도만큼 방향으로 이동
    for i in range(len(fire_ball)):
        r = fire_ball[i][0]
        c = fire_ball[i][1]
        m = fire_ball[i][2]
        s = fire_ball[i][3]
        d = fire_ball[i][4]
        ny = (dy[d]*s) + c
        nx = (dx[d]*s)+ r
        if ny == N:
            ny = 0
        elif ny == 0:
            ny = N
        if nx == N:
            nx = 0
        elif nx == 0:
            nx = N


        fire_ball[i][0] = nx
        fire_ball[i][1] = ny
    
    
    fire_ball = sorted(fire_ball, key=lambda x:(x[0],x[1]))
    for i in range(len(fire_ball)-1,0,-1):
        if fire_ball[i][0] == fire_ball[-1][0] and fire_ball[i][1] == fire_ball[-1][1]:
            fire_ball[i-1][2] = fire_ball[i-1][2]+fire_ball[i][2]
            fire_ball[i-1][3] = fire_ball[i-1][3]+fire_ball[i][3]
            fire_ball[i-1][8] = fire_ball[i-1][8]+fire_ball[i][8]
            fire_ball[i-1][5] = 1
            if fire_ball[i-1][4] //2 == 1:
                fire_ball[i-1][6] = 1
            elif fire_ball[i-1][4] //2 == 0:
                fire_ball[i-1][7] = 1
            fire_ball.pop(i)
    
    for i in range(len(fire_ball)-1,0,-1):
        if fire_ball[i][2]:
            tmp1 = fire_ball[i][2]//5
            tmp2 = fire_ball[i][3]//fire_ball[i][8]
            if fire_ball[i][5] and tmp1:
                if fire_ball[i][6] and fire_ball[i][7]:
                    fire_ball.append([ fire_ball[i][0], fire_ball[i][1], tmp1, tmp2, 1, fire_ball[i][5], 0,0,1])
                    fire_ball.append([ fire_ball[i][0], fire_ball[i][1], tmp1, tmp2, 3, fire_ball[i][5], 0,0,1])
                    fire_ball.append([ fire_ball[i][0], fire_ball[i][1], tmp1, tmp2, 5, fire_ball[i][5], 0,0,1])
                    fire_ball.append([ fire_ball[i][0], fire_ball[i][1], tmp1, tmp2, 7, fire_ball[i][5], 0,0,1])
                elif (fire_ball[i][6] == 0 and fire_ball[i][7] == 1) or (fire_ball[i][6] == 1 and fire_ball[i][7] == 0):
                    fire_ball.append([ fire_ball[i][0], fire_ball[i][1], tmp1, tmp2, 0, fire_ball[i][5], 0,0,1])
                    fire_ball.append([ fire_ball[i][0], fire_ball[i][1], tmp1, tmp2, 2, fire_ball[i][5], 0,0,1])
                    fire_ball.append([ fire_ball[i][0], fire_ball[i][1], tmp1, tmp2, 4, fire_ball[i][5], 0,0,1])
                    fire_ball.append([ fire_ball[i][0], fire_ball[i][1], tmp1, tmp2, 6, fire_ball[i][5], 0,0,1])
        fire_ball.pop(i)
    for f in fire_ball:
        print(f)
    print()
ret = 0
for fire in fire_ball:
    ret += fire[2]
print(ret)



    
    