//진짜 바보같이푼 거
T = int(input())
for test in range(T):
    P = input().rstrip()
    Q = input().rstrip()
    res = 0
    idx = []
    oh = []
    check = 0
    print("#{}".format(test+1),end=' ')
    if len(P) == len(Q):
        for i in range(len(P)):
            res+=ord(Q[i])-ord(P[i])
            check = ord(Q[i])-ord(P[i])
            if check >= 1:
                idx.append(i)
                if check == 1 and i == len(P) - 2:
                    oh.append(1)
            elif check == -25 and i == len(P) - 1:
                oh.append(-25)
        if len(oh) > 1:
            if oh[0] == 1 and oh[1] == -25:
                print('N')
            else:
                print('Y')
        elif res > 1 or idx[0] < len(P):
            print('Y') 
        else:
            print('N')

    elif len(P) + 1 == len(Q):
        for i in range(len(P)):
            res+=ord(Q[i])-ord(P[i])
            check = ord(Q[i])-ord(P[i])
            if check == 1:
                idx.append(i)
        if res == 0:
            if Q[len(P)] == 'a':
                print('N')
            else:
                print('Y')
        elif res > 1 or idx[0] < len(P):
            print('Y')
        else:
            print('N')
    else:
        print('Y')

//이렇게 해도 됨
for T in range(int(input())):
    P = input().rstrip()
    Q = input().rstrip()
    if P + "a" != Q:
        result = "Y"
    else:
        result = "N"

    print(f'#{T + 1} {result}')