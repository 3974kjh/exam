T = int(input())
for test in range(T):
    N,M = map(int, input().split())
    t = []
    for i in range(30):
        t.append(M%2)
        M = int(M/2)
    count = 0
    for i in range(N):
        if t[i] == 1:
            count+=1
    print("#{}".format(test+1),end=' ')
    if count == N:
        print('ON')
    else:
        print('OFF')