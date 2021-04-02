T = int(input())
for test in range(T):
    l = int(input())
    num = list(map(int, input().split()))
    i = 1
    LIS = []
    LIS.append(num[0])
    while (i < l):
        count = 0
        for k in range(len(LIS)):
            if (LIS[k] <= num[i]):
                count+=1
            elif (LIS[len(LIS)-1] > num[i]):
                del(LIS[k])
                LIS.append(num[i])
                LIS.sort()
                break
        if (count == len(LIS)):
            LIS.append(num[i])
        i+=1
        
    print("#{}".format(test+1), end=' ')
    print(len(LIS))