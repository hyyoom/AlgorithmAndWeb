import sys
sys.stdin = open("text.txt", "r")

# 번호가 작은 물고기부터 순서대로 이동.
# 물고기는 한 칸을 이동할 수 있음.
# 상어가 있거나, 경계 넘어가면 못감
# 못가면 45도 반시계 회전시킴. -> 다 봤는데 이동 불가하면 이동 x
# 그 외에는 그 칸으로 이동 -> 서로 위치를 바꾸는 방식으로 이동함

# 물고기 먼저 이동하면 상어가 이동함.

N,M = map(int,input().split())
cars = list(map(int,input().split()))
m = [[int(input())] for _ in range(M)]
cars.sort()
m.sort()
m_len = len(m)
cars_len = len(cars)
j = 0
# i * len-i
for i in range(len(cars)):
    if j<=m_len and cars[i] == m[j][0]:
        m[j].append(i*(cars_len-i-1))
        j+=1
    if j>m_len:
        break
    

for s in m:
    if len(s) == 1:
        s.append(0)
    
print(cars, m)
