T = int(input())


def power_set(idx,N,total):
    global cnt

    if idx == N:
        # print(used)
        if total == M:
            cnt += 1
        return
    
    used[idx] = 1
    power_set(idx+1,N,total+nums[idx])
    used[idx] = 0
    power_set(idx+1,N,total)


for tc in range(1,T+1):
    N,M = map(int, input().split())
    nums = list(map(int, input().split()))
    
    used = [0] * N
    cnt = 0
    
    power_set(0,N,0)
    print(f"#{tc} {cnt}")