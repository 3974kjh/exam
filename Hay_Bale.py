T = int(input())
for test in range(T):
    N = int(input())
    S = []
    while len(S) != N:
        S.append(int(input()))
    S_m = int(sum(S) / len(S))
    res = 0
    for i in range(len(S)):
        if (S[i] < S_m):
            res+=S_m - S[i]
    print("#{}".format(test+1),end=' ')
    print(res)