T = int(input())



# v를 루트로 하는 서브트리의 노드의 갯수
def solve(v):
    if v == 0: # 노드가 아님
        return 0
    # 왼쪽 서브트리 노드 갯수, 오른쪽 서브트리 노드 갯수, + 1
    return solve(tree[0][v]) + solve(tree[1][v]) + 1
          # 왼쪽 서브트리 + 오른쪽 서브트리 + 루트?




for tc in range(1, T+1):
    E, N = map(int,input().split())
    data = list(map(int,input().split()))
    V = E+1

    tree = [[0]*(V+1) for _ in range(2)]

    for i in range(0,E*2,2):
        p, c = data[i], data[i+1]
        if tree[0][p] == 0:
            tree[0][p] = c
        else:
            tree[1][p] = c
    

    result = solve(N)
    print(result)
    # 트리는 일종의 그래프이기에 bfs,dfs도 가능함.
    # 트리순회방법 : 전위, 중위, 후위 (사실은 dfs임)