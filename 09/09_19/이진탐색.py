arr = [2,4,7,9,11,19,23]

def binary_search1(arr, key):
    # 중간값 찾고
    # key랑 중간값이랑 비교해서
    # 다르면, 절반은 버리고, 나머지 절반에서 다시 탐색 시작
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return True
        # 어떤 절반을 버릴지 결정
        if arr[mid] < key:
            start = mid+1
        elif arr[mid] > key:
            end = mid-1
    return False

# 주어진 범위 안에 key가 있는지 없는지 반환하는 함수
def binary_search_recur(arr,key,s,e):
    if s > e:
        return False
    mid = (s+e)//2
    if arr[mid] == key:
        return True
    if arr[mid] < key:
        return binary_search_recur(arr,key,mid+1,e)
    elif arr[mid] > key:
        return binary_search_recur(arr,key,s,mid-1)


print(binary_search1(arr,11))
print(binary_search_recur(arr,1,0,len(arr)-1))

            
        

        

