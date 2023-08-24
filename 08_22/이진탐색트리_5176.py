T = int(input())

def inorder(n):
    global cnt
    if n > N:
        return
    # if n <= N: # 둘다 가능
    inorder(n*2)
    tree[n] = cnt
    cnt += 1
    inorder(n*2+1)


for tc in range(1, T+1):
    N = int(input())
    cnt = 1

    tree = [0] * (N+1)
    inorder(1)
    print(tree)