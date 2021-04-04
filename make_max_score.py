T = int(input())
for test in range(T):
    N,K = map(int, input().split())
    score = list(map(int, input().split()))
    score = sorted(score, reverse=True)
    res = 0
    for i in range(K):
        res+=score[i]
    print("#{}".format(test+1), end=' ')
    print(res)