'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

'''

def preorder(n): # 전위 순회
    if n: # 존재하는 정점이면
        print(n) # visit(n) not visited!
        preorder(ch1[n]) # 왼쪽 서브트리로 이동
        preorder(ch2[n])




V = int(input())
E = V-1 # 트리의 간선 수 = 정점 수 - 1


arr = list(map(int, input().split()))
# 부모를 인덱스로 자식을 저장
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

for i in range(E):
    p,c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

preorder(1)