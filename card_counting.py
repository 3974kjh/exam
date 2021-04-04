T = int(input())
for test in range(T):
    card = list(map(str, input()))
    res = [13,13,13,13]
    flag = 0
    kk = 0
    for j in range(len(card)/3-1):
        k = 2
        for i in range(len(card)/3 - 1 - j):
            if (card[j+kk] == card[j+kk+k+i+1] and card[j+kk+1] == card[j+kk+k+i+2] and card[j+kk+2] == card[j+kk+k+i+3]):
                print("#{}".format(test+1), end=' ')
                print("ERROR")
                flag = 1
                break
            k+=2
        if (flag == 1):
            break
        kk+=2
    if (flag != 1):
        for i in range(len(card)):
            if card[i] == 'S':
                res[0] = res[0] - 1
            elif card[i] == 'D':
                res[1] = res[1] - 1
            elif card[i] == 'H':
                res[2] = res[2] - 1
            elif card[i] == 'C':
                res[3] = res[3] - 1
        
        print("#{}".format(test+1),end=' ')
        for i in range(len(res) - 1):
            print(res[i], end=' ')
        print(res[len(res)-1])