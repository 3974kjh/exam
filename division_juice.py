T = int(input())
for test in range(T):
    N = int(input())
    print("#{}".format(test+1),end = ' ')
    for i in range(N-1):
        print("1/{}".format(N),end=' ')
    print("1/{}".format(N))
        