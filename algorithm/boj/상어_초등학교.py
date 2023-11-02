N = int(input())
dy = [-1,1,0,0]
dx = [0,0,-1,1]


students = []
stu_likes = []
for _ in range(N**2):
    tmp = list(map(int,input().split()))
    students.append(tmp.pop(0))
    stu_likes.append(tmp)



maps = [[0]*N for _ in range(N)]
tmp = students.pop(0)
maps[1][1] = tmp


stu_likes.pop(0)

for stu_like in stu_likes:
    directions = []
    directions_2 = []
    directions_3 = []
    tmp = students.pop(0)

    # 1번조건
    for r in range(N):
        for c in range(N):
            cnt = 0
            for k in range(4):
                nr = dy[k]+r
                nc = dx[k]+c
                if 0<=nr<N and 0<=nc<N:
                    if maps[nr][nc] in stu_like:
                        cnt += 1
            directions.append([r,c,cnt])
    directions.sort(key=lambda x:(-x[2]))

    for i in range(1,len(directions)):
        if directions[0][2] == directions[i][2]:
            directions_2.append(directions[i])
        else:
            break
    directions_2.append(directions[0])
    
    if len(directions_2) == 1:
        maps[directions_2[0][0]][directions_2[0][1]] = tmp
        directions_2 = []
        continue

    # 두번째 조건
    for i in range(len(directions_2)):
        cnt = 0
        for k in range(4):
            nr = dy[k]+directions_2[i][0]
            nc = dx[k]+directions_2[i][1]
            if 0<=nr<N and 0<=nc<N:
                if not maps[nr][nc]: # 비었다면
                    cnt += 1
        directions_2[i][2] = cnt
    
    # 세번째 조건
    directions_3 = []

    directions_2.sort(key=lambda x:(-x[2]))
    
    for i in range(1,len(directions_2)):
        if directions_2[0][2] == directions_2[i][2]:
            directions_3.append(directions_2[i])
        else:
            break
    print(directions_2)
    directions_3.append(directions_2[0])
    
    if len(directions_3) == 1:
        maps[directions_3[0][0]][directions_3[0][1]] = tmp
        print(directions_3,"di333333")
        print(tmp)
        directions_3=[]
        continue

    directions_3.sort(key=lambda x:(x[1],x[2]))
    print(directions_3)
    # print(directions_3)
    # print(stu_like,"asdfdsfas")
    maps[directions_3[0][0]][directions_3[0][1]] = tmp

for m in maps:
    print(m)











