arr = [2,4,7,9,11,19,23]

arr.sort()

def binarysearch_recur(target, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    if target == arr[mid]:
        return mid
    if target > arr[mid]:
        return binarysearch_recur(target,mid+1,high)
    else:
        return binarysearch_recur(target,low,mid-1)

print(binarysearch_recur(7,0,len(arr)-1))


def binarysearch(target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

print(binarysearch(11))