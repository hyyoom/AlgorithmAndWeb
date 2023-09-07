T = int(input())

dic = {"0001101": 0, "0011001" : 1, "0010011":2, "0111101":3,
       "0100011": 4, "0110001" : 5, "0101111":6, "0111011":7,
        "0110111":8, "0001011" :9}


for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    data = [input().strip() for _ in range(N)]
    use = ''
    for i in range(N):
        if "1" in data[i]:
            use = data[i][:]
            break
    idx = 0
    for i in range(len(use)-1,-1,-1):
        if use[i] == "1":
            idx = i
            break
    
    use = use[idx-55:idx+1]
    
    ret = []
    for i in range(0,56,7):
        ret.append(dic[use[i:i+7]])
    
    even = 0
    odd = 0
    result = 0
    for i in range(len(ret)):
        if i % 2 == 0:
            odd += ret[i]
        else:
            even += ret[i]
    result = even + (odd*3)
    if result%10 == 0:
        print(f"#{tc} {sum(ret)}")
    else:
        print(f"#{tc} 0")

    
    