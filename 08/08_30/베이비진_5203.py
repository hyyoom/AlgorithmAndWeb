T = int(input())


def permutation(cards, k, target, result,v,player):
    if k == target:
        # print(cards, result)
        result.sort()
        if result[2] == result[1]+1 == result[0]+2 or\
            result[0] == result[1] == result[2]:
            return player
        return 0
    
    for i in range(len(cards)):
        if not v[i]:
            v[i] = 1
            r1 = permutation(cards,k+1,target,result+[cards[i]],v,player)
            v[i] = 0
            if r1:
                return r1
    return 0
            



for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    while cards:
        p1.append(cards.pop(0))
        p2.append(cards.pop(0))
    
    idx = 0
    winner = 0
    flag = 0
    for target in range(3,7):
        v = [0] * 6
        winner = permutation(p1[:target],0,3,[],v,1)
        if winner:
            print(f"#{tc} {winner}")
            flag = 1
            break
        winner = permutation(p2[:target],0,3,[],v,2)
        if winner:
            print(f"#{tc} {winner}")
            flag = 1
            break
        idx += 1
    if not winner:
        print(f"#{tc} {winner}")
