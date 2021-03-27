T = int(input())
for test in range(T):
    num = int(input())
    A = []
    for a in range(num):
        B = list(map(str, input()))
        A.append(B)
    res = 0
    count = 1
    k = 2
    kk = -1
    n = int(num / 2)
    for i in range(num):
        for j in range(count):
            if (int(num / 2) == i):
                k = -2
                kk = 1
            res+=int(A[i][j + n])
        count = count + k
        n = n + kk
    print("#{}".format(test+1), end=' ')
    print(res)