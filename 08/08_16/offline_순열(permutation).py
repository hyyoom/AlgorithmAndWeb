# 위의 순서를 다 바꿔보는걸 순열이라 함.
# 123,132,213,231,312,321 == 순열


#perm_arr idx에 들어갈 수 있는 애들 다 넣어보기

#중복순열 = 나온애들 또 나옴, 111 112 113 121 123 131 132등
def perm(idx):
    if idx == N:
        print(perm_arr)
        return
    for i in range(N):
        perm_arr[idx] = arr[i]
        perm(idx+1)

# 중복되지 않은 순열
def perm1(idx,used):
    if idx == N:
        print(perm_arr)
        return
    for i in range(N):
        # 앞에서 쓴 것은 쓰지않음
        if used[i] == 0:
            perm_arr[idx] = arr[i]
            used[i] = 1
            perm1(idx+1,used)
            used[i] = 0


def perm2(idx): # 완탐, 할 수 있는거 다해봄, 안바꾸거나, 뒤에요소랑 자리 바꾸거나
    if idx == N:
        print(arr)
    for i in range(idx, N): # 나 포함해서 뒤에 있는애랑 바꿈
        arr[idx], arr[i] = arr[i], arr[idx]
        perm2(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]


arr = [1,2,3]
N = 3
perm_arr = [0] * N
used = [0]*N
perm2(0)