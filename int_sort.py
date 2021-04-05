T = int(input())
for test in range(T):
    N = int(input())
    d = []
    while N != len(d):
        d.extend(map(int, input().split()))
    res = []
    if N <= 10:
        for i in range(N):
            res.append(d[i])
        for i in range(N-1):
            res.append(d[i]*10 + d[i+1])
    elif N > 10:
        for i in range(N):
            res.append(d[i])
        for i in range(N-1):
            res.append(d[i]*10 + d[i+1])
        for i in range(N-2):
            res.append(d[i]*100 + d[i+1]*10 + d[i+2])
    elif N > 100:
        for i in range(N):
            res.append(d[i])
        for i in range(N-1):
            res.append(d[i]*10 + d[i+1])
        for i in range(N-2):
            res.append(d[i]*100 + d[i+1]*10 + d[i+2])
        for i in range(N-3):
            res.append(d[i]*1000 + d[i+1]*100 + d[i+2]*10 + d[i+3])
    res.sort()
    here = [res[0]]
    i = 0
    while (len(res) - 1 > i):
        if (res[i] != res[i+1]):
            here.append(res[i+1])
        i+=1
    flag = 0
    k = 0
    for i in range(len(here)):
        if i != here[i]:
            print("#{}".format(test+1),end=' ')
            print(i)
            flag = 1
            break
        k = i
    if (flag == 0):
        print("#{}".format(test+1),end=' ')
        print(here[k] + 1)