T = int(input())

for tc in range(1,T+1):
    N,M,L = map(int, input().split())
    tree = [0] * (N+1)
    
    for _ in range(M):
        a, b = map(int,input().split())
        tree[a] = b
    
    
    for i in range(N//2,0,-1):
        if i*2+1 <= N:
            tree[i] = tree[i*2] + tree[i*2+1]
        elif i*2+1 > N:
            tree[i] = tree[i*2]
        
    print(f"#{tc} {tree[L]}")