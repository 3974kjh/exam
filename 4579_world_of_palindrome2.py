T = int(input())
for test in range(T):
    n = input()
    flag = 0
    print("#{}".format(test+1),end=' ')
    if flag == 0:
        count = 0
        n = list(map(str, n))
        j = len(n) - 1
        for i in range(int(len(n)/2)):
            if not(n[i] == n[j] or n[i] == '*' or n[j] == '*'):
                flag = 1
                break
            elif n[i] == '*' or n[j] == '*':
                flag = 0
                break
            elif n[i] == n[j]:
                count+=1
            j-=1
        if count == int(len(n)/2) or flag == 0:
            print('Exist')
        else:
            print('Not exist')