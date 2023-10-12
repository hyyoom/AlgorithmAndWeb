N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

tmp = ''

for c in range(M):
    dic = {chr(x):0 for x in range(ord('A'), ord('Z')+1)}
    for r in range(N):
        dic[arr[r][c]] += 1
    dic_val = list(dic.values())
    maxv = max(dic_val)
    for i in range(len(dic_val)):
        if dic_val[i] == maxv:
            tmp += chr(ord('A')+i)
            break

print(tmp)

answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != tmp[j]:
            answer+=1
print(answer)


