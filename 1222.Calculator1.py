for test in range(10):
    N = int(input())
    k = list(map(str, input()))
    res = []
    for i in k:
        if '0' <= i <= '9':
            res.append(int(i))
    print("#{} {}".format(test+1, sum(res)))