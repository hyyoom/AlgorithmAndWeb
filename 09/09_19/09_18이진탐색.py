T = int(input())

#이전 탐색에서 오른쪽을 봤는지, 왼쪽을 봤는지 알아야함
#연속 2개는 안됨.
# 0은 탐색 시작, 1은 왼쪽 2는 오른쪽
def binary_search(A,key):
    dir = 0
    # A안에 키가 있는지 확인 + 방향이 바뀌어 가면서 위치하는가
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if A[mid] == key:
            return True
        if A[mid] < key:
            if dir == 2:
                return False
            dir = 2
            start = mid+1
        elif A[mid] > key:
            if dir == 1:
                return False
            dir = 1
            end = mid-1
    return False

for tc in range(1, T+1):
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for num in B:
        if binary_search(A,num):
            cnt += 1
    print(f"#{tc} {cnt}")


# 3
# 3 3
# 1 2 3
# 2 3 4
# 3 5
# 1 3 5
# 2 4 6 8 10
# 5 5
# 1 3 5 7 9
# 1 2 3 4 5