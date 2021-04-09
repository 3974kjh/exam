T = int(input())
for test in range(T):
    N = int(input())
    d = []
    for i in range(N):
        a = int(input())
        d.append(a)
    first = d[0]
    count = 1
    res = []
    for i in range(1,len(d)):
        res.append(d[i] - first)
    l = len(res)

    while l > 0:
        k = 1
        for i in range(l-1):
            if res[k] % res[0] != 0:
                k+=1
            else:
                del(res[k])
        del(res[0])
        l = len(res)
        if l > 0:
            count+=1
        
    print("#{} {}".format(test+1,count))