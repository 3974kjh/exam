T = int(input())
for test in range(T):
    n = input()
    flag = 0
    no = ['aa','aab','ana','aaaaa']
    for i in range(4):
        if n == no[i]:
            flag = 1
            break
    print("#{}".format(test+1),end=' ')
    if flag == 0:
        count = 0
        n = list(map(str, n))
        j = len(n) - 1
        for i in range(int(len(n)/2)):
            if n[i] == n[j] or n[i] == '?' or n[j] == '?':
                count+=1
            j-=1
        if count == int(len(n)/2):
            print('Exist')
        else:
            print('Not exist')
    else:
        print('Not exist')