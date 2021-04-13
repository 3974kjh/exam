T = int(input())
for test in range(T):
    N = int(input())
    i = 1
    res = 0
    flag = 0
    if N >= 1000:
        i = 10
    elif N >= 100000:
        i = 100
    elif N >= 1000000000:
        i = 1000
    elif N >= 1000000000000:
        i = 10000
    elif N >= 1000000000000000:
        i = 100000
    while i**3 <= N:
        if i**3 == N:
            flag = 1
            res = i
            break
        i+=1
    print("#{}".format(test+1),end=' ')
    if flag == 1:
        print(res)
    else:
        print(-1)