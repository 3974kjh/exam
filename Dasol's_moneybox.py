T = int(input())
for test in range(T):
    N = int(input())
    res = 0
    for i in range(N):
        p, x = map(float, input().split())
        res+=p * x
    print("#{}".format(test+1),end=' ')
    print('%f' %res)