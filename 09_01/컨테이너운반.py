T = int(input())
for tc in range(1, T+1):
    N,M= map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    # 큰 트럭이 최대한 큰 물건을 가지고 가게
    trucks = sorted(trucks, reverse=True)
    containers = sorted(containers, reverse=True)
    
    total = 0
    j = 0

    v = [0] * len(containers)
    for i in range(len(trucks)):
        while j < len(containers):
            if not v[j]:
                if trucks[i] >= containers[j]:
                    total += containers[j]
                    v[j] = 1
                    break
            j+=1

    print(f"#{tc} {total}")