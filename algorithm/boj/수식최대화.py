import copy

operation = []
nums = []

def solve(idx,N,v,result,op):
    global operation
    if idx == N:
        operation.append(result)
        return
    for i in range(N):
        if not v[i]:
            v[i] = 1
            solve(idx+1,N,v,result+[op[i]],op)
            v[i] = 0

def solution(expre):
    global nums
    tmp = ''
    arr = []
    op = []

    i = 0
    while i < len(expre):
        if expre[i] == '-' or expre[i] == '*' or expre[i] == '+':
            arr.append(expre[i])
        else:
            while i<len(expre):
                if ord('0')<=ord(expre[i])<=ord('9'):
                    tmp += expre[i]
                else:
                    arr.append(int(tmp))
                    tmp = ''
                    i-=1
                    break
                i+=1
        i+=1
    while i < len(expre):
        tmp += expre[i]
    arr.append(int(tmp))
    
    for k in range(len(arr)):
        if arr[k] == '*' or arr[k] == '-' or arr[k] ==  '+':
            op.append(arr[k])
    op = list(set(op))
    v = [0]*len(op)
    solve(0,len(op),v,[],op)
    nums = arr[:]



expre = "50*6-3*2"
solution(expre)



ret = []
st = []
check = []
result = []

for opra in operation:
    tmp = copy.deepcopy(nums)
    for op in opra:
        i = 1
        while i < len(tmp):
            if tmp[i] == op:
                one = tmp.pop(i-1)
                two = tmp.pop(i)
                tmp.pop(i-1)
                if op == '+':
                    tmp.insert(i-1, one+two)
                elif op == '-':
                    tmp.insert(i-1, one-two)
                elif op == '*':
                    tmp.insert(i-1, one*two)
            i+=1

    s = 0
    if len(tmp) == 3:
        if tmp[1] == '-':
            s = tmp[0] - tmp[2]
        elif tmp[1] == '+':
            s = tmp[0] + tmp[2]
        elif tmp[1] == '*':
            s = tmp[0] * tmp[2]
        tmp = 0
        tmp = s
    else:
        s = tmp[0]
        tmp = s
            
    result.append(abs(tmp))
    tmp = []

print(max(result))


# print(operation, nums)