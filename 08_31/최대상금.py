T = int(input())

answer = []
def f(cnt):
    if cnt == M:
        answer.append(nums[:])
        return
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            nums[i],nums[j] = nums[j],nums[i]
            f(cnt+1)
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1,T+1):
    N,M = map(int, input().split())

    nums = list(str(N))
    f(0)
    
    # for i in range(len(answer)):
    #     if answer[i]:
    #         answer[i] = int("".join(answer[i]))
    
    tmp = "".join(max(answer))
    print(f"#{tc} {tmp}")