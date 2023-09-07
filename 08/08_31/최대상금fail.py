T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())

    nums = list(str(N))
    nums_sort_rev = sorted(nums, reverse=True)
    nums_sort = sorted(nums)

    for i in range(len(nums)):
        M-=1
        if nums[i] != nums_sort_rev[i]:
            tmp = nums_sort_rev[i]
            for j in range(len(nums)-1,-1,-1):
                if nums[j] == nums_sort_rev[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        if M <= 0:
            break
    else:
        M+=1
        while M:
            nums[len(nums)-1], nums[len(nums)-2] = nums[len(nums)-2], nums[len(nums)-1]
            M-=1

    print(f"#{tc}",end=" ") 
    print("".join(nums))