T = int(input())
for test in range(T):
    N = int(input())
    station = []
    for i in range(N):
        A = list(map(int, input().split()))
        station.extend(A)
    bus = []
    res = []
    P = int(input())
    for i in range(P):
        B = input()
        bus.append(B)
        res.append(0)
    bus = list(map(int, bus))
    k = 0
    for i in range(N):
        for z in range(len(bus)):
            if station[i+k] <= bus[z] and bus[z] <= station[i+k+1]:
                res[z] = res[z] + 1
        k+=1
    print("#{}".format(test+1),end=' ')
    for i in range(len(res)):
        print(res[i],end=' ')
    print('')