# 부분집합, 조합, 순열
a = [1,2,3,4,5]
N = len(a)
selected = [0]*N

def power_set(idx, N): # 모든 부분집합을 구함
    if idx == N:
        for i in range(N):
            if selected[i] == 1:
                print(a[i], end=" ")
        print()
        return
    selected[idx] = 1
    power_set(idx+1,N)
    selected[idx] = 0
    power_set(idx+1,N)



def combination(idx,N,k,target):
    if k == target:
        for i in range(N):
            if selected[i] == 1:
                print(a[i], end=" ")
        print()
        return
    
    if idx == N:
        # for i in range(N):
        #     if selected[i] == 1:
        #         print(a[i], end=" ")
        # print()
        return
    selected[idx] = 1
    combination(idx+1,N,k+1,target)
    selected[idx] = 0
    combination(idx+1,N,k,target)


v = [0]*N
def permutation(idx,N,result):
    if idx == N:
        print(result)
        return
    for i in range(N):
        if not v[i]:
            v[i] = 1
            permutation(idx+1,N,result+[a[i]])
            v[i] = 0

# power_set(0,3)
# combination(0,N,0,2)
permutation(0,N,[])