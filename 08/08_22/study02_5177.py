
# 힙 만들어서 삽입하는 연산

def heap_push(data):
    global heap_pointer
    # 완전 이진트리 유지를 위해서
    # 이진트리의 마지막(heap_pointer) 넣어주고
    heap[heap_pointer] = data

    # 방금 넣은 요소가 heap조건 만족하는지 확인
    # 아니면 바꿔주기

    child = heap_pointer
    parent = child//2

    while parent > 0 and heap[child] < heap[parent]:
        # 작은애가 위로 올라감, 최소힙
        heap[child], heap[parent] = heap[parent], heap[child]
        child = parent
        parent = child//2
    
    heap_pointer += 1
T = int(input())
for tc in range(1,T+1):
    # heap 역할을 할 이진트리를 배열로 만듬
    N = int(input())
    heap = [0] * (N+1)
    # 어느 위치에 요소가 들어가야 하는지 알려주는 변수 필요
    heap_pointer = 1
    arr = list(map(int,input().split()))
    for i in arr:
        heap_push(i)
    ret = 0
    while N > 0:
        N //= 2
        ret += heap[N]
    print(f"#{tc} {ret}")