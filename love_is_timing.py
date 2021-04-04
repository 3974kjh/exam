T = int(input())
for test in range(T):
    a = list(map(int, input().split()))
    p = 0
    if (a[0] < 11 or (a[0] == 11 and a[1] < 11)):
        p = -1
    elif (a[0] == 11 and a[1] == 11 and a[2] == 11):
        p = 0
    else:
        res = []
        res.append(a[0] - 11)
        res.append(a[1] - 11)
        res.append(a[2])
        here = 0
        here+=res[0] * 24 * 60
        here+=res[1] * 60
        here+=res[2] - 11
        p = here
    print("#{}".format(test+1),end=' ')
    print(p)        