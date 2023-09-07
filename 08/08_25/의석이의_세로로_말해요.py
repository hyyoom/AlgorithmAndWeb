T = int(input())
for tc in range(1,T+1):

    data = [list(input().strip()) for _ in range(5)]
    
    maxv = 0
    for i in data:
        if len(i) >= maxv:
            maxv = len(i)
    
    for i in range(5):
        while len(data[i]) < maxv:
            data[i].append("-1")

    tmp = [[] for _ in range(maxv)]
    for i in range(maxv):
        if len(data) > i:
            tmp[i] = data[i]
        else:
            j = 0
            while j < maxv:
                tmp[i].append("-1")
                j+=1 
    
    result = ''    
    for i in range(maxv):
        for j in range(maxv):
            if tmp[j][i] != "-1":
                result += tmp[j][i]

    print(f"#{tc} {result}")