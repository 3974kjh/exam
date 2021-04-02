T = int(input())
for test in range(T):
    L = int(input())
    card_all = list(map(str, input().split()))
    card1 = []
    card2 = []
    res = []
    flag = 0
    if L % 2 == 0:
        for i in range(L):
            if int(L/2) <= i:
                card2.append(card_all[i])
            else:
                card1.append(card_all[i])
    else:
        flag = 1
        for i in range(len(card_all)):
            if (int(L/2))+1 <= i:
                card2.append(card_all[i])
            else:
                card1.append(card_all[i])
    
    for i in range(len(card1)):
        res.append(card1[i])
        if (flag == 1 and i == len(card1) - 1):
            break
        res.append(card2[i])

    print("#{}".format(test+1), end = ' ')
    for i in range(L-1):
        print(res[i], end=' ')
    print(res[L-1])