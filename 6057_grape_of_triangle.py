T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    here = []
    for i in range(M):
        k = list(map(int, input().split()))
        here.extend(k)
    n = 0
    array = [[0] * 0 for i in range(N+1)]
    for i in range(int(len(here)/2)):
        for j in range(1,51):
            if here[i+n] == j:
                array[j].append(here[i+n+1])
        n+=1
    res = 0
    for i in range(1, N - 1):
        for z in range(i, N - 1):
            count = 0
            flag = 0
            for j in range(len(array[i])):
                for k in range(len(array[z+1])):
                    if z+1 == array[i][j]:
                        flag = 1
                    if array[i][j] == array[z+1][k]:
                        count+=1
            if flag == 1:
                res+=count
    print("#{} {}".format(test+1, res))