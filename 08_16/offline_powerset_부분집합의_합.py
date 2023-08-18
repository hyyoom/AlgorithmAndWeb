# 1-10 원소의 합이 10인 부분집합을 구하라

def solve(idx,sum_v):
    # idx번째 요소를 부분집합에 포함 하느냐 마느냐
    # 필요없는 경우의 수 수행하지 않기 위한 중간합이 필요
    if sum_v > 10: # 가능성 없음
        return
    if sum_v == 10: # 찾는 부분
        # print(selected)
        for i in range(N):
            if selected[i]:
                print(arr[i], end=" ")
        print()
        return
    if idx == N: # 마지막까지 봤는데 10보다 작은 상태
        return
    selected[idx]=1
    solve(idx+1,sum_v+arr[idx])
    selected[idx]=0
    solve(idx+1,sum_v)



arr = [1,2,3,4,5,6,7,8,9,10]
N = 10
selected = [0]*N
solve(0,0)