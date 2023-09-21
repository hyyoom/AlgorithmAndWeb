T = int(input())
# 각 정류장에서 배터리를 갈아 끼우거나 아니거나 모두 다 해보기
# remain : 현재 배터리 잔량
def solve(idx,remain, cnt):
    global min_cnt
    if idx == N-1:
        if min_cnt > cnt:
            min_cnt = cnt
        return
    if cnt>=min_cnt:
        return
    # 배터리를 갈아끼기
    remain-=1
    solve(idx+1, data[idx], cnt+1)
    if remain > 0:
        solve(idx+1, remain, cnt)
    # 배터리를 갈아끼지 않기



for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = data.pop(0)
    min_cnt = 100
    solve(1,data[0],0)
    print(f"#{tc} {min_cnt}")

    
    