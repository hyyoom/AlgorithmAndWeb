T = int(input())

for tc in range(1, T+1):
    N, nums = input().split()
    N = int(N)
    nums = list(nums)
    tmp = ''
    ret = ''
    for i in nums:
        tmp = bin(int(i, base=16))[2:]
        cnt = 4 - len(tmp)
        ret += "0"*cnt+tmp 
    print(f"#{tc} {ret}")