# 중위 표현식으로 풀면 됨.


for tc in range(1,11):

    ret = 0
    def solve(n):
        if n:                      # 현재 노드가 존재하는 정점일 때
            #solve(n*2) #완전 이진트리 일때는 이렇게 씀
            #solve(n*2+1)
            solve(ch1[n])         # 왼쪽 자식
            solve(ch2[n])        # 오른쪽 자식
            # '+-*/' 연산자에 대한 계산 : 왼쪽과 오른쪽을 불러오고 난 후 -> 후위계산?
            # tree[n] 값에 각 연산자가 올 때 왼쪽 자식과 오른쪽 자식을 불러와서 그 연산 결과 만들어주기
            if parent[n] == '+':      # + 일떄
                parent[n] = int(parent[ch1[n]]) + int(parent[ch2[n]])
            elif parent[n] == '-':    # - 일때
                parent[n] = int(parent[ch1[n]]) - int(parent[ch2[n]])
            elif parent[n] == '*':    # * 일때
                parent[n] = int(parent[ch1[n]]) * int(parent[ch2[n]])
            elif parent[n] == '/':    # / 일때
                parent[n] = int(parent[ch1[n]]) // int(parent[ch2[n]]) # 소수점은 버리므로 // 로 계산
    

    V = int(input())
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    parent = [0] * (V+1)

    for i in range(V):
        data = list(input().split())
        if len(data) == 2:
            parent[int(data[0])] = int(data[1])
        else:
            ch1[int(data[0])] = int(data[2])
            ch2[int(data[0])] = int(data[3])
            parent[int(data[0])] = data[1]
    solve(1)
    print(f"#{tc} {parent[1]}")
    # print(ch1, ch2, parent)


