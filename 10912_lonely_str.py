T = int(input())
for test in range(T):
    n = list(map(str, input()))
    n.sort()
    l = len(n)-1
    k = 0
    i = 0
    while (l > k):
        if n[i] == n[i+1]:
            del(n[i])
            del(n[i])
            k+=2
        else:
            i+=1
            k+=1
    print("#{}".format(test+1),end=' ')
    if (len(n) == 0):
        print('Good')
    else:
        for i in range(len(n)):
            print(n[i],end='')
        print('')