T = int(input())
for test in range(T):
    N = int(input())
    k = list(map(int, input().split()))
    k_mean = int(sum(k) / len(k))
    count = 0
    for i in range(len(k)):
        if k[i] <= k_mean:
            count+=1
    print("#{}".format(test+1),end=' ')
    print(count)