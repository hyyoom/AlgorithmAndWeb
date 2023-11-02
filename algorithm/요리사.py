T = int(input())

def synergy(lst):
    total = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            total += foods[lst[i]][lst[j]] + foods[lst[j]][lst[i]]
    return total

def solve(idx,target,N,results):
    global ans
    if idx == N:
        if len(results) != N//2:
            return
        lst1 = results
        lst2 = []
        for i in chk:
            if i not in lst1:
                lst2.append(i)
        total_A = synergy(lst1)
        total_B = synergy(lst2)
        ans = min(ans, abs(total_A - total_B))
        return
    
    solve(idx+1,target+1,N,results+[chk[idx]])
    solve(idx+1,target,N,results)


for tc in range(1,T+1):
    N = int(input())
    ans = 999999
    foods = [list(map(int, input().split())) for _ in range(N)]
    # v = [0]*(N)
    chk = [x for x in range(0,N)]
    solve(0,N//2,N,[])
    print(f'#{tc} {ans}')