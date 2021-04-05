T = int(input())
for test in range(T):
    N,K = map(int, input().split())
    n = list(map(int, input().split()))
    n.sort()
    res = []
    k = 0
    for i in range(1, N+1):
        if (k < K and i != n[k]):
            res.append(i)
        elif (k < K and i == n[k]):
            k+=1
        else:
            res.append(i)
    print("#{}".format(test+1),end=' ')
    for i in range(len(res)-1):
        print(res[i], end=' ')
    print(res[len(res)-1])