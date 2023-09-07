T = int(input())


def solve(cnt, checked):
    tmp = int("".join(nums))
    global maxv
    if cnt==N:
        # 최대 상금 구하기
        if maxv < tmp:
            maxv = tmp
        return
    
    if (cnt, tmp) in checked:
        return
    # 중복연산 방지
    checked.add((cnt,tmp))

    for i in range(l-1):
        for j in range(i+1,l):
            nums[i], nums[j] = nums[j],nums[i]
            # 한번 교환한 상태
            solve(cnt+1, checked) # 두번째 교환 세번째 교환 쭉 교환하러
            nums[i], nums[j] = nums[j],nums[i]


for tc in range(1, T+1):
    nums, N = input().split()
    N = int(N)
    l = len(nums)
    nums = list(nums)
    maxv = 0
    # checked = set()
    solve(0,set())
    print(f"#{tc} {maxv}")