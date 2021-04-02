T = int(input())
for test in range(T):
    i = 0
    k = list(map(int,input().split()))
    if k[0] <= k[2] and k[2] <= k[1]:
        i = 0
    elif k[2] > k[1]:
        i = -1
    else:
        i = k[0] - k[2]
    print("#{}".format(test+1),end=' ')
    print(i)