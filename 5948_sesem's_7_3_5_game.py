T = int(input())
for test in range(T):
    n = list(map(int, input().split()))
    n.sort(reverse=True)
    res = []
    for k in range(5):
        for i in range(5-k):
            for j in range(5-i-k):
                res.append(n[k]+n[k+i+1]+n[k+i+2+j])
    
    k = len(res)
    j = 0
    res.sort(reverse=True)
    for i in range(k-1):
        if res[j] == res[j+1]:
            del(res[j+1])
        else:
            j+=1
    print("#{}".format(test+1),end=' ')
    print(res[4])