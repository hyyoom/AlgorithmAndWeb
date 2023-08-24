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


# 1. 입력사이에서 (2진)암호코드 찾아내기
# 2. (2진)암호코드를 이루는 숫자(10진수 암호코드) 찾아내기
# 3. (10진수)암호코드가 정상인지 판단
# 4. 결과 출력

def solve(data):
    #행은 위에서 아래로.. 열은 뒤에서 앞으로 보면서 코드찾기
    for i in range(N):
        for j in range(M-1,54,-1): # 55번 까지 확인하고 없으면 없는거
            if data[i][j] == 1: #암호코드 찾음!
                #지금부터....숫자 8개 읽어오기
                code = []
                for _ in range(8):
                    #숫자 1개 읽어오기
                    w1 = w2 = w3 = w4 = 0
                    #1의 개수 세기..
                    while data[i][j] == 1:
                        w4 += 1
                        j -= 1
                    #0의 개수 세기..
                    while data[i][j] == 0:
                        w3 += 1
                        j -= 1
                    #1의 개수 세기..
                    while data[i][j] == 1:
                        w2 += 1
                        j -= 1
                    #0의 개수 안세고 구하기..
                    w1 = 7 - w2 - w3 - w4
                    j -= w1
                    code.insert(0,code_dic[(w1,w2,w3,w4)])
                # 암호코드(code)가 정상인지 아닌지 판별
                odd_sum = code[0] + code[2] + code[4] + code[6]
                even_sum = code[1] + code[3] + code[5] + code[7]
                if (odd_sum*3 + even_sum) % 10 == 0:
                    return odd_sum + even_sum
                else:
                    return 0

                # return code


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    data = [list(map(int,input())) for _ in range(N)]
    result = solve(data)
    print(f'#{tc} {result}')
