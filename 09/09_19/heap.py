#heap의 조건
#1.완전이진트리
#2.부모>자식 또는 부모<자식

#완전 이진트리는 배열로 만들거다~

heap = [None] * 100
#heap_pointer:새로운 요소가 들어갈 위치
heap_pointer = 1 
#루트가 1번에서 시작하니까

def heap_push(data):
    global heap_pointer
    heap[heap_pointer]=data
    #최대힙일 경우엔 더 크다면 부모랑 자리 바꾸기
    # 반복, 부모보다 작거나, 루트가 되면 중단
    current = heap_pointer
    parent = current//2
    while parent > 0 and heap[parent] < heap[current]:
        heap[parent],heap[current] = heap[current],heap[parent]
        current = parent
        parent = current//2
    heap_pointer+=1



def heap_pop():
    result = heap[1]
    if heap_pointer == 1: #heap비어잇음
        return None
    heap[1] = heap[heap_pointer-1]
    parent = 1
    child = parent * 2 # 왼쪽 자식으로 선언
    # 자식들 중에 더 큰값 선택해서 부모노드값이랑 비교
    if child + 1 <= heap_pointer: # 오른쪽 자식이 존재한다는 뜻


heap_push(4)
heap_push(1)
heap_push(2)
heap_push(6)
heap_push(2)
heap_push(5)
heap_push(7)
heap_push(9)
print(heap)

