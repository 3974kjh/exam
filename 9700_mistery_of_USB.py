T = int(input())
for test in range(T):
    p,q = map(float, input().split())
    s1 = 1 - (p * q)
    s1_f = 1 - (p * (1 - q))
    s2 = 1 - (s1_f * q)
    print("#{}".format(test+1),end=' ')
    if (s1 < s2):
        print('YES')
    else:
        print('NO')