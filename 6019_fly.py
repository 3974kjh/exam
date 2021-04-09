T = int(input())
for test in range(T):
    n = list(map(float, input().split()))
    time = n[0] / (n[1] + n[2])
    res = n[3] * time
    print("#{}".format(test+1),end=' ')
    print('%.6f' %res)