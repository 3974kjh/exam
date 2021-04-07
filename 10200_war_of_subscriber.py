T = int(input())
for test in range(T):
    k = list(map(int, input().split()))
    t_f = min(k[1],k[2])
    if (k[0] < k[1]+k[2]):
        t_n_f = abs(k[0] - (k[1] + k[2]))
    else:
        t_n_f = 0
    print("#{}".format(test+1),end =' ')
    print(t_f, t_n_f)
