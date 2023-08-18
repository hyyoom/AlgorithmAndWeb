for tc in range(1,11):
    T = int(input())
    secret = list(map(int, input().split()))

    minus = 1
    while True:
        if secret[7] == 0:
            break
        if minus == 6:
            minus = 1
        tmp = secret.pop(0)
        if tmp - minus >= 0:
            tmp -= minus
        else:
            tmp = 0
        secret.append(tmp)
        minus += 1
    secret = map(str, secret)
    print(f"#{T}", " ".join(secret))