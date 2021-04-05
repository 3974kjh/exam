T = int(input())
for test in range(T):
    n = list(map(str, input()))
    print("#{}".format(test+1),end=' ')
    if int(n[len(n)-1]) % 2 == 1:
        print('Odd')
    else:
        print('Even')