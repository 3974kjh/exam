T = int(input())
for test in range(T):
    N,Q = input().split()
    here = []
    for i in range(int(Q)):
        here_q = list(map(int, input().split()))
        here.append(here_q)
    res = []
    for i in range(int(N)):
        res.append(0)
    for i in range(int(Q)):
        for j in range(here[i][0]-1, here[i][1]):
            res[j] = i+1
    print("#{}".format(test+1),end=' ')
    for i in range(len(res)-1):
        print(res[i],end=' ')
    print(res[len(res)-1])
