from collections import deque
T = int(input())
minv = 0xfffff

def bfs(q_start, end_point):
    result = []
    time = maps[end_point[0]][end_point[1]]
    for q in q_start:
        result.append(abs(q[0]-end_point[0]) + abs(q[1]-end_point[1]))
    result.sort()
    if result and len(result) <= 3:
        return max(result) + time + 1
    
    # 리턴에 +1해서 하기
    if result:
        result[0] += time + 1
        result[1] += time + 1
        result[2] += time + 1
        for i in range(3,len(result)):
            if result[i-3] + time + 1 == result[i]:
                result[i] = result[i]+time
            elif result[i-3] < result[i]:
                result[i] = result[i]+time + 1
            else:
                tmp = result[i-3]+result[i]+time
                result[i] += tmp
        return result[len(result)-1]
    return 0

def combination(i,target,result):
    global minv
    if i == target:
        tmp1 = []
        tmp2 = []
        for re in range(1,person_cnt+1):
            if re in result:
                tmp1.append(person[re])
            else:
                tmp2.append(person[re])
        solve1 = bfs(tmp1,stare[0])
        solve2 = bfs(tmp2,stare[1])
        if solve2 <= solve1:
            tmp = solve1
        else:
            tmp = solve2
        if minv > tmp:
            minv = tmp
        return
    combination(i+1, target, result+[i])
    combination(i+1, target, result)


for tc in range(1,T+1):
    N = int(input())
    maps = [list(map(int,input().split())) for _ in range(N)]
    person = []
    person_cnt = 0
    stare = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                person.append((i,j))
                person_cnt += 1
            elif maps[i][j] > 1:
                stare.append((i,j))

    person.insert(0,[])
    person_cnt_list = [x for x in range(1,person_cnt+1)]
    combination(1,N+1,[])
    print(f"#{tc} {minv}")
    minv = 0x99999
    


