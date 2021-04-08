T = int(input())
for test in range(T):
    n = int(input())
    k = list(map(int, input().split()))
    k.sort(reverse=True)
    res = []
    count = 0
    j = 0
    for i in range(len(k)-1):
        if (k[j] == k[i]):
            count+=1
        else:
            res.append(k[j])
            res.append(count)
            if len(res) > 2:
                if (res[1] < res[3]):
                    res.pop(0)
                    res.pop(0)
                else:
                    del(res[2])
                    del(res[2])
            j = i + 1
            count=0
    print("#{}".format(test+1),end=' ')
    print(res[0])