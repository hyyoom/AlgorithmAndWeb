# 활동 = 시작, 종료       종료시간을 기준으로 정렬
T = int(input())


for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int,input().split())) for _ in range(N)]
    # 활동선택 문제- 가장 많은 활동을 하기 위한 선택
    # 1.종료시간을 기준으로 정렬함
    # 2.먼저 끝나는 순서대로 정렬되어 있음.. 먼저 끝나는 활동을 선택함
    # 3.이전 선택활동과 겹치면 선택하면 안됨, 안겹치면 선택
    times = sorted(times, key=lambda x:x[1])
    cnt = 0
    prev = 0 # 0시부터
    for time in times:
        if time[0] >= prev:
            cnt += 1
            prev = time[1]
    print(f"#{tc} {cnt}")