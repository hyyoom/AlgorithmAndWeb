T = int(input())

di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

for tc in range(1, T+1):
    N,M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    # 기본위치
    t = N//2
    board[t][t] = board[t-1][t-1] = 2
    board[t-1][t] = board[t][t-1] = 1
    for _ in range(M):
        a,b,color = map(int, input().split())
        board[b-1][a-1] = color
        for d in range(8):
            i = b-1 + di[d]
            j = a-1 + dj[d]
            # 같은 생깔 찾으면 바꾸면서 돌아올거임
            while 0<=i<N and 0<=j<N:
                if board[i][j] == 0:
                    break
                elif board[i][j] != color:
                    i += di[d]
                    j += dj[d]
                else:
                    # 멈추고 돌 바꾸기
                    # 현재 위치부터 
                    while True:
                        i -= di[d]
                        j -= dj[d]
                        if i == b-1 and j == a-1:
                            break
                        board[i][j] = color
                    break
    
    bcnt = 0
    wcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                bcnt+=1
            elif board[i][j] == 2:
                wcnt+=1
    print(f"#{tc} {bcnt} {wcnt}")



        