def merge_sort(arr,s,e): #인덱스 이동을 이용해서 merge작성
    if s==e:
        return
    mid = (s+e)//2
    # 절반을 각각 정렬한 상태여야 한다.
    merge_sort(arr,s,mid)
    merge_sort(arr,mid+1,e)
    i = s
    j = mid+1
    tmp = []
    while j <= e and i <= mid:
        # i랑 j랑 비교해서 더 작은 애를 복사하고 인덱스 증가
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            j+=1
    while i<=mid:
        tmp.append(arr[i])
        i+=1
    while j<=e:
        tmp.append(arr[j])
        j+=1
    j = 0
    for i in range(s, e+1):
        arr[i] = tmp[j]
        j+=1

arr=[7,2,1,10,3,11,7,34]
merge_sort(arr,0,len(arr)-1)
print(arr)