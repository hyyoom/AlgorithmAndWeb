T = int(input())
cnt = 0

def merge_sort(arr,s,e):
    global cnt
    if s==e:
        return
    mid = (s+e)//2
    merge_sort(arr,s,mid)
    merge_sort(arr,mid+1,e)
    i = s
    j = mid+1
    # 0 1 2 3 4
    tmp = []
    while i<=mid and j<=e:
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
    for i in range(s,e+1):
        arr[i] = tmp[j]
        j+=1
    if arr[mid] > arr[e]:
        cnt += 1

for tc in range(1,T+1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, N-1)
    print(f"#{tc} {arr[N//2]} {cnt+1}")