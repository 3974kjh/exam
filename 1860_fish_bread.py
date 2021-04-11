T = int(input())
for test in range(T):
    N,M,K = map(int, input().split())
    n = list(map(int, input().split()))
    n.sort()
    t = [0] * 11112
    for i in range(N):
        t[n[i]]-=1
    print("#{}".format(test+1),end=' ')

    if n[0] < M:
        print('Impossible')
    else:
        j = 1
        for i in range(int(n[len(n)-1]/M)):
            t[M*j]+=K
            j+=1
        if sum(t) < 0:
            print('Impossible')
        else:
            here = 0
            flag = 0
            for i in range(len(t)):
                here+=t[i]
                if here < 0:
                    print('Impossible')
                    flag = 1
                    break
            if flag == 0:
                print('Possible')