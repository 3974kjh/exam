for test in range(10):
    n = int(input())
    k = list(map(int, input().split()))
    res = 0
    for i in range(2,n-2):
        if k[i-2] < k[i] and k[i-1] < k[i] and k[i+1] < k[i] and k[i+2] < k[i]:
            sc_max = max(k[i-2],k[i-1],k[i+1],k[i+2])
            res+=k[i]-sc_max
    print("#{}".format(test+1),end =' ')
    print(res)