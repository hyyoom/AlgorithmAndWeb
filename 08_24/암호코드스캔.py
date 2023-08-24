# 16진수 2진수로 변환 과정
# 16진수 > 10진수 > 2진수
def hex_to_decimal(h):
    hex_dic = {
        'a' : 10,
        'b' : 11,
        'c' : 12,
        'd' : 13,
        'e' : 14,
        'f' : 15
    }
    result = 0
    for chr in h:
        if chr in '0123456789':
            num = int(chr)
        else:
            num = hex_dic[chr]

        result = result*16 + num
    return result
# print(hex_to_decimal('1a'))
def decimal_to_binary(number):
    binary = ''
    while number:
        remain = number % 2
        number //= 2
        if remain:
            binary = '1' + binary
        else:
            binary = '0' + binary

    while len(binary) % 4:
        binary = '0'+ binary
    return binary

print(decimal_to_binary(hex_to_decimal('1ffff')))


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

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    data = [list(map(int,input())) for _ in range(N)]
    
