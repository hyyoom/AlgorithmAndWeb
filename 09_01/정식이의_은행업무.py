T = int(input())
for tc in range(1, T+1):
    A = input()
    B = list(map(int, input()))

    N = len(A)
    M = len(B)
    ans = 0

    binary = int(A, 2)
    bin_list = [0]*N
    # print(binary)
    for i in range(N):
        bin_list[i] = binary^(1<<i) # 비트 반전
    
    for i in range(M):
        num1 = 0
        num2 = 0
        for j in range(M):
            if i!=j:
                num1 = num1*3 + B[j]
                num2 = num2*3 + B[j]
            else:
                num1 = num1*3 + (B[j]+1)%3
                num2 = num2*3 + (B[j]+2)%3
        if num1 in bin_list:
            ans = num1
            break
        if num2 in bin_list:
            ans = num2
            break
    print(f"#{tc} {ans}")
