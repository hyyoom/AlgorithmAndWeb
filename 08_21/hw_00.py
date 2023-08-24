
for tc in range(1, 11):
    N = int(input())

    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)

    word = [[] for _ in range(N+1)]
    for i in range(1,N+1):
        data = list(input().split())
        word[i].append(data[1])
        if len(data) == 3:
            ch1[i] = int(data[2])
        elif len(data) == 4:
            ch1[i] = int(data[2])
            ch2[i] = int(data[3])

    order= []
    def in_order(n):
        global order
        
        if n:
            in_order(ch1[n])
            order.append(n)
            in_order(ch2[n])
            
    in_order(1)

    print(f"#{tc} ",end="")
    for i in order:
        print("".join(word[i]),end="")
    print()
