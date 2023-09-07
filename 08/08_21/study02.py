def preorder(n):
    global cnt
    if n <= N:
        preorder(n * 2)
        tree[n] = cnt
        cnt += 1
        preorder(n * 2 + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)

    cnt = 1
    preorder(1)
    print(tree)

    print(f'#{tc} {tree[1]} {tree[N // 2]}')