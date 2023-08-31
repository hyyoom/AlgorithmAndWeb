a = [3,6,7,1,5,4]
N = 6
subset1 = []

# for i in range(1, (1<<N)-1): # 2의 N제곱
for i in range(1, (1<<N)//2):
    subset1 = []
    subset2 = []
    # total1 = 0
    # total2 = 0
    for j in range(N):
        if i & (1<<j): # j번 비트가 0 이 아니면
            subset1.append(a[j])
            # total1 += a[j]
        else:
            subset2.append(a[j])
            # total1 += a[j]
    
    print(subset1, subset2)
    