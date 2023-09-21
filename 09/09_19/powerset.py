arr = [i for i in range(1,4)]
path = [0] * 3

def power(idx, N):
    if idx == N:
        print(*path)
        return
    for num in arr:
        path[idx] = num
        power(idx+1,N)
        path[idx] = num

print(power(0,3))


arr = [1,2,3]
path2 = [0] * 3

def power2(idx, N):
    if idx == N:
        print(path2)
        return
    for num in arr:
        if num in path2:
            continue
        path2[idx] = num
        power2(idx+1,N)
        path2[idx] = 0

print(power2(0,3))