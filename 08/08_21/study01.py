T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    V = E+1

    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    cnt = 0
    def preorder(n): # 전위 순회
        global cnt
        if n: # 존재하는 정점이면
            cnt += 1
            preorder(ch1[n]) # 왼쪽 서브트리로 이동
            preorder(ch2[n])
    preorder(N)

    print(f"#{tc} {cnt}")
