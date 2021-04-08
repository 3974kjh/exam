T = int(input())
for test in range(T):
    N = int(input())
    here = []
    for i in range(N):
        k = list(map(int, input().split()))
        here.extend(k)
    count = 0
    k = 0
    for i in range(int(len(here)/2)-1):
        kk=2
        for j in range(int(len(here)/2)-1-i):
            if here[k] > here[kk+k] and here[k+1] < here[kk+k+1]:
                count+=1
            elif here[k] < here[kk+k] and here[k+1] > here[kk+k+1]:
                count+=1
            kk+=2
        k+=2
    print("#{} {}".format(test+1, count))
