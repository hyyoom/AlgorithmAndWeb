
a = [1,2,3]
b = [0,0,0]

def f(i, N):
    if i == N:
        return
    else:
        b[i] = a[i]
        f(i+1, N)

f(0,3)
print(b)