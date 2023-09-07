# 1. 16->10, 10->2
alpha = [chr(i) for i in range(ord("A"), ord("F")+1)]
make_dict_num = [i for i in range(10, 16)]
code_dic = {
(3,2,1,1) : 0,
(2,2,2,1) : 1,
(2,1,2,2) : 2,
(1,4,1,1) : 3,
(1,1,3,2) : 4,
(1,2,3,1) : 5,
(1,1,1,4) : 6,
(1,3,1,2) : 7,
(1,2,1,3) : 8,
(3,1,1,2) : 9
}



def d_to_b(nums):
    bi = ''
    if nums == 0:
        bi = "0000"
    else:
        while nums:
            tmp = nums%2
            nums //= 2
            if tmp:
                bi = "1"+bi
            else:
                bi = "0"+bi
        while len(bi) % 4:
            bi = "0"+bi
    

    return bi
        

def h_to_d(nums):
    dic = dict(zip(alpha, make_dict_num))
    result = 0
    ret = 0
    for num in nums:
        if num in "0123456789":
            ret = int(num)
        else:
            ret = dic[num]
        result = result*16 + ret
    return result



def find_multiple(data):
    for i in range(len(data)):
        if data[i]:
            lens = len(data[i])
            for j in range(lens-1,-1,-1):
                if data[i][j] == "1":
                    w1 = w2 = w3 = w4 = 0
                    while data[i][j] == "1":
                        w4 += 1
                        j -= 1
                    while data[i][j] == "0":
                        w3 += 1
                        j -= 1
                    while data[i][j] == "1":
                        w2 += 1
                        j -= 1
                    return min(w2,w3,w4)

def make_numbers(data,multiple):
    data_i_len = len(data)
    code = []
    for i in range(data_i_len-1):
        if data[i]:
            for j in range(len(data[i][0])-1, -1, -1):
                if data[i][0][j] == "1":
                    for _ in range(8):                    
                        w1 = w2 = w3 = w4 = 0
                        while data[i][0][j] == "1":
                            w4 += 1
                            j -= 1
                        while data[i][0][j] == "0":
                            w3 += 1
                            j -= 1
                        while data[i][0][j] == "1":
                            w2 += 1
                            j -= 1
                        
                        w1 = 7-w4-w3-w2
                        j -= w1
                        code.insert(0,code_dic[(w1//1,w2//1,w3//1,w4//1)])
                        # code.insert(0,(w1//multiple,w2//multiple,w3//multiple,w4//multiple))
                        print(w1,w2,w3,w4,end=" ")
    # print(data[3])
    print(code)




T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    datas = [input().strip() for _ in range(N)]
    data = [[] for _ in range(N)]
    for i in range(N):
        data[i].append(d_to_b(h_to_d(datas[i])))
    
    multiple = find_multiple(data)
    for i in range(len(data)):
        data[i][0] = "0"*100 + data[i][0]
    # print(data)
    make_numbers(data,multiple)
