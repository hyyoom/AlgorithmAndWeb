# N*N 크기의 행렬에 N개의 퀸을 놓아보기~~~~~~~~
# row번 행에 퀸하나 놓기

N = 4
board = [[0]*N for _ in range(N)]
# 가지 치기를 위해 행 확인 chk_col
chk_col = [0] * N

# 대각선 r+c가 같다면 오른쪽위에서 왼쪽밑 대각선
# r-c가 같다면 반대의 같은 대각선에 있는거다
chk_dia1 = [0]*(2*N-1)
chk_dia2 = [0]*(2*N-1)


def nqueen(row):
    if row == N:
        for r in board:
            print(r)
        print("---------------")
        return
    # 모든 열에 놓아보고, 놓아지면, 놓고 다음행으로 놓으러 가기
    for i in range(N):
        # i번 열에 퀸 놓아 보기
        if not chk_col[i] and not chk_dia1[row+i] and not chk_dia2[row-i+N-1]: # 열 중복확인
            board[row][i] += 1
            chk_col[i] += 1
            chk_dia1[row+i] += 1
            chk_dia2[row-i+N-1] += 1
            nqueen(row+1)
            board[row][i] -=1
            chk_col[i] -=1
            chk_dia1[row+i] -=1
            chk_dia2[row-i+N-1] -=1

nqueen(0)
