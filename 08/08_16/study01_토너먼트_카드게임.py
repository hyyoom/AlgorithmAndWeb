

# start 부터 end까지 범위의 승자를 반환하는 함수
def solve(start, end):
    # return 승자
    if start == end: # 한명이라면
        return start
    m = (start+end) // 2
    
    w1 = solve(start, m) # 각 그룹의 승자의 번호
    # data[w1] data[w2] 각 승자들이 낸 모양
    w2 = solve(m+1, end)

# def solve(start, end) :
#     if start == end:
#         return end # start 상관없음
#     m = (start+end) // 2
#     w1 = solve(start, m)
#     w2 = solve(m+1, end)
#     if card[w1] == 1:
#         if card[w2] == 2:
#             return w2
#         else:
#             return w1
#     if card[w1] == 2:
#         if card[w2] == 1:
#             return w1
#         elif card[w2] == 3:
#             return w2
#         else:
#             return w1
#     if card[w1] == 3:
#         if card[w2] == 1:
#             return w2
#         elif card[w2] == 2:
#             return w1
#         else:
#             return w1
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    print(f"#{tc} {solve(0,N-1)+1}")
