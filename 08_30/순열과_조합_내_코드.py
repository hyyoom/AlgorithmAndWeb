#combination : 조합
#전략 => 뽑을래 말램 o,x 로 나뉨

a = [1,2,3,4,5]
answer = []
N = 5

def combination(idx, k, target, result):
    if target == k:
        answer.append(result)
        # print(result)
        return
    if idx == N:
        return
    combination(idx+1, k+1, target, result+[a[idx]])
    combination(idx+1, k, target, result)

# combination(0,0,3,[])
# print(answer)




#permutation : 순열
#전략 -> visited, 전부확인

visited = [0] * len(a)

def permutation(k, target, visited, result):
    if k == target:
        answer.append(result)
        return
    for i in range(len(a)):
        if not visited[i]:
            visited[i] = 1
            permutation(k+1,target,visited,result+[a[i]])
            visited[i] = 0

permutation(0,5,visited,[])
print(answer)

