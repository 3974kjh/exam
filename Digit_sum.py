T = int(input())
res = []
for test in range(T):
    n = int(input())
    n = str(n)
    while (1):
        if len(n) == 1:
            res.append(n)
            break
        else:
            here = []
            for i in range(len(n)):
                here.append(int(n[i]))
            n = str(sum(here))
for i in range(T):
    print("#{}".format(i+1),end =' ')
    print(res[i])