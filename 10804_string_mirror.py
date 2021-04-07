T = int(input())
for test in range(T):
    n = list(map(str, input()))
    i = 1
    res = []
    while len(n)-i >= 0:
        res.append(n[len(n)-i])
        i+=1
    print("#{}".format(test+1),end = ' ')
    for i in range(len(res)):
        if res[i] == 'b':
            print('d',end='')
        elif res[i] == 'd':
            print('b',end='')
        elif res[i] == 'q':
            print('p',end='')
        elif res[i] == 'p':
            print('q',end='')
    print('')