# 후위 순회 결과 반환하는 함수
def post_order(v):
    # if tree[v][0] not in ["*","/","+","-"]:
    #     return tree[v][0]
    if type(tree[v][0]) == int:
        return tree[v][0]
    else:
        left = post_order(tree[v][1])
        right = post_order(tree[v][2])
        if tree[v][0] == "+":
            return left+right
        elif tree[v][0] == "-":
            return left-right
        elif tree[v][0] == "*":
            return left*right        
        elif tree[v][0] == "/":
            return left//right

for tc in range(1,11):
    N = int(input())
    tree = [[0] * 3 for _ in range(N+1)] # 반대로 해도 됨

    for _ in range(N):
        node = input().split()
        if node[1] in "+-/*":
            num = int(node[0])
            tree[num][0] = node[1]
            tree[num][1] = int(node[2])
            tree[num][2] = int(node[3])
        else:
            tree[int(node[0])][0] = int(node[1])
    
    print(post_order(1))