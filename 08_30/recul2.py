N = 5
A = [1,2,3,4,5]
B = [0] * N
key = 33

# key가 있으면 1 없으면 0리턴
def f1(i, N, key, arr): # 현재값, 목표값, 찾고자하는 key원소
    if i == N: # 현재 == 목표
        return 0 # 키가 없는 경우
    elif arr[i] == key:
        return 1
    else:
        return f1(i+1, N, key, arr) #값을 전달해줌
print(f1(0, N, key, A))

