
def binarysearch_recur(target, low, high, left, right, flag):
    if low > high:
        return -1
    mid = (low+high)//2
    if target == arr[mid]:
        return mid
    if target > arr[mid]:
        if left==False:
            return binarysearch_recur(target,mid+1,high,True,False,0)
    else:
        if right==False:
            return binarysearch_recur(target,low,mid-1,False,True,0)
    

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    find_num = list(map(int, input().split()))

    for find in find_num:
        binarysearch_recur(find, 0, len(arr), False, False, 0)