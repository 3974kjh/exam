T = int(input())
for test in range(T):
    k = []
    for i in range(5):
        n = list(map(str, input()))
        k.append(n)
    max_len = max(len(k[0]),len(k[1]),len(k[2]),len(k[3]),len(k[4]))
    res = []
    for i in range(max_len):
        for j in range(5):
            if (i <= len(k[j])-1):
                res.append(k[j][i])
    print("#{}".format(test+1),end=' ')
    for i in range(len(res)-1):
        print(res[i],end='')
    print(res[len(res)-1])