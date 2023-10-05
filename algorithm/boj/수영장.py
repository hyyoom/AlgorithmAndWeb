from collections import deque


def bfs(start,each_price):
    q=deque()
    q.append((start,0))
    minv = each_price[3]
    while q:
        m,price = q.popleft()
        if m > 12:
            if price < minv:
                minv = price
        for i in range(3):
            if i == 0 and m<=12:
                next_m = m+1
                next_price = price + (swim[m]*each_price[i])
                q.append((next_m, next_price))
            elif i == 1 and m<=12:
                next_m = m+1
                next_price = price + each_price[i]
                q.append((next_m, next_price))
            elif i == 2 and m<=12:
                next_m = m+3
                next_price = price + each_price[i]
                q.append((next_m, next_price))
    return minv
 
T = int(input())
for tc in range(1,T+1):
    each_price = list(map(int,input().split()))
    swim = list(map(int, input().split()))
    swim = [-1] + swim
    for i in range(1,len(swim)):
        if swim[i] != 0:
            start = i
            break
    print(f"#{tc} {bfs(start,each_price)}")