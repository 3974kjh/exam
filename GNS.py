T = int(input())
for test in range(T):
    n = input().split()
    num = input().split()
    check_num = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    for i in range(len(num)):
        for j in range(10):
            if (num[i] == check_num[j]):
                del(num[i])
                num.insert(i,j)
                break
    num.sort()
    print("#{}".format(test+1))
    for i in range(len(num)-1):
        for j in range(10):
            if (num[i] == j):
                print(check_num[j],end =' ')
    for j in range(10):
        if (num[len(num)-1] == j):
            print(check_num[j])
