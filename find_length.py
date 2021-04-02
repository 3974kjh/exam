T = int(input())
for test in range(T):
    l = list(map(int,input().split()))
    if l[0] == l[2]:
        del(l[2])
        del(l[0])
    elif l[0] == l[1]:
        del(l[1])
        del(l[0])
    else:
        del(l[1])
        del(l[1])
    print("#{}".format(test+1),end=' ')
    print(l[0])