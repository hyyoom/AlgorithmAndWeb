
s = 0
def solve(i,s,v): # y
    global sum_v
    global N
    if i == N:
        if sum_v > s:
            sum_v = s
        return
    if s > sum_v:
        return
    for j in range(N):
        if not v[j]:
            v[j] = 1
            solve(i+1,s+nums[i][j],v)
            v[j] = 0
            
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    sum_v = 10000
    s = 0
    v = [0] * N # 0이면 해당하는 열에 퀸 없음
    solve(0,s,v)
    print(f"#{tc} {sum_v}")


# 4881. 배열 최소 합 [D2]

# def solve(i, N, s, visited):
#     global sum_v        # 최소 합 변수 글로벌 선언
#     if i == N:
#         if sum_v > s:   # 현재 값 s가 sum_v보다 작을 경우
#             sum_v = s   # 최소 합으로  업데이트 해주는 조건문
#     elif s > sum_v:     # 최소 합보다 더 크게나오면 진행 X
#         return
#     else:
#         for j in range(N):
#             if not visited[j]:  # 아직 방문하지 않은 곳이 있다면
#                 visited[j] = 1  # 해당하는 곳을 +1로 표시
#                 solve(i+1, N, s+arr[i][j], visited) # 다음 위치로 이동
#                 visited[j] = 0  # 이동하고나면 다시 -1

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     sum_v = 10000   # 최소 합 초기화 : 대충 100....? 정도로
#                   # 습관적으로 0 으로 설정했었는데 생각을 다시해보니 입력받는 정수가 0보다 작게나올순 없다
#     visited = [0] * N   # 방문 표시할 visited 배열 생성

#     solve(0, N, 0, visited)
#     print(f'#{tc} {sum_v}')





