# 활동 = 시작, 종료       종료시간을 기준으로 정렬
T = int(input())

# def power_set(idx, N):
#     if idx == N:
#         for i in range(len(selected)):
#             if selected[i] == 1:
#                 print(i, end=" ")
#         print()
#         return
    # selected[idx] = 1
    # power_set(idx+1, N)
    # selected[idx] = 0
    # power_set(idx+1, N)


def power_set(idx, lst):
    if idx == N:
        # 이곳에서 계산해서 출력..

        
        return
    lst.append(times[idx])
    power_set(idx+1, lst)
    lst.pop(0)
    power_set(idx+1, lst)



for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int,input().split())) for _ in range(N)]
    times = sorted(times, key=lambda x:x[1])

    # 1. 종료시간 순으로 정렬
    # 2. 활동의 모든 부분 집합을 생성.
    # 3. 생성한 부분집합끼리 겹치는지 확인하고 안겹치면 갯수세기
    
    selected = [0] * N
    # power_set(0, N)
    lst = []
    power_set(0, lst)



    # print(f"#{tc} {cnt}")