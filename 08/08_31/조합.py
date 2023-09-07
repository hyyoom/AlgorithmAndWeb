# used = [0] * 5
# arr = [1,2,3,4,5]

# def com(i, k, target,N,result):
#     if k == target:
#         print(result)
#         return
#     if i == N:
#         return  
#     com(i+1,k+1,target,N,result+[arr[i]])
#     com(i+1,k,target,N,result)

# com(0,0,3,5,[])


arr = [-1,3,-1,6,7,-6,1,5,4,-2]
used = [0] * len(arr)

def power_set(i,N,total):
    if i == N:
        if total == 0:
            print(used)
        return
    used[i] = 1
    power_set(i+1,N,total+arr[i])
    used[i] = 0
    power_set(i+1,N,total)

power_set(0,len(arr),0)
