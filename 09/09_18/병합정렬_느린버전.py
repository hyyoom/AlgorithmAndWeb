
T = int(input())
cnt = 0

def merge_sort(arr): #시간 복잡도 느린 버전
    global cnt
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    arr1=merge_sort(arr[:mid]) #정렬되어 있는 배열이라 침
    arr2=merge_sort(arr[mid:])
    new_arr=[]
    if arr1[-1] > arr2[-1]:
        cnt += 1
    len_left = len(arr1)
    len_right = len(arr2)
    i = 0
    j = 0
    while i<=len_left and j<=len_right:
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i+=1
        else:
            new_arr.append(arr2[j])
            j+=1
    while i<=len_left:
        new_arr.append(arr1[i])
        i+=1
    while j<=len_right:
        new_arr.append(arr2[j])
        j+=1

    return new_arr

for tc in range(1,T+1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = merge_sort(arr)
    print(f"#{tc} {tmp[N//2]} {cnt}")