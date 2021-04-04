T = int(input())
for test in range(T):
    n = int(input())
    sow = [1,1,1,2]
    if n - 1 > 3:
        for i in range(3,n-1):
            sow.append(sow[i-2] + sow[i-1])
        print("#{}".format(test+1), end=' ')
        print(sow[n-1])
    else:
        print("#{}".format(test+1), end=' ')
        print(sow[n-1])