# 한 행에 하나의 퀸을 놓아보기
# 만약 모든 행에 퀸을 다 놓았다면 N개의 퀸을 놓은 것 = 해를 찾은 것
cnt = 0
def solve(row): # y
    global cnt
    if row == N:
        cnt += 1
        return 
    # row행에 모든 열에 퀸 놓아보기
    for col in range(N):
        # row, col에 놓을 수 있으면 퀸 놓아보기
        if not col_check[col] and not dia_check1[row+col]\
            and not dia_check2[N-1+row-col]:
            col_check[col] += 1
            dia_check1[row+col] += 1
            dia_check2[N-1+row-col] += 1
            solve(row+1)
            col_check[col] -= 1
            dia_check1[row+col] -= 1
            dia_check2[N-1+row-col] -= 1
            

# N = int(input())
N = 18

# 열 사용 가능여부 표시 배열
col_check = [0] * N # 0이면 해당하는 열에 퀸 없음
# 대각선 사용 가능여부 표시 배열
dia_check1 = [0] * (N*2-1) # r+c
dia_check2 = [0] * (N*2-1) # N-1 + r-c
solve(0)
print(cnt)






