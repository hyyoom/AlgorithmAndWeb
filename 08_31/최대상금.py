T = int(input())

answer = []
# def solve(idx,result):
#     if idx == M:
#         if result not in answer:
#             answer.append(result)
#             # answer.append(result)
#             # print(result)
#         return 
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             nums[i],nums[j] = nums[j],nums[i]
#             solve(idx+1,result+[nums[:]])
#             nums[j],nums[i] = nums[i],nums[j]

def f(cnt):
    if cnt == M:
        answer.append(nums[:])
        return
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            nums[i],nums[j] = nums[j],nums[i]
            # print(nums)
            f(cnt+1)
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1,T+1):
    N,M = map(int, input().split())

    nums = list(str(N))
    f(0)
    
    for i in range(len(answer)):
        answer[i] = int("".join(answer[i]))
    print(answer)