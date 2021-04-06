T = int(input())
for test in range(T):
    n = list(map(int,input().split()))
    min = n[0]
    if (n[0] > n[1]):
        min = n[1]
    count = 0
    mon = n[2]
    while min <= mon:
        mon = mon - min
        count+=1
    print("#{}".format(test+1),end=' ')
    print(count)
