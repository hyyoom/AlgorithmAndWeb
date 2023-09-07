for test in range(1, 11):
    N = int(input())
    sums = []
    tmp = []
    building = list(map(int, input().split()))
    for i in range(2, len(building)-2):
        tmp.append(building[i-1])
        tmp.append(building[i-2])
        tmp.append(building[i+1])
        tmp.append(building[i+2])
        if building[i] < max(tmp):
            sums.append(max(tmp) - building[i])
        tmp = []
        print(f"#{test} {sum(sums)}")
