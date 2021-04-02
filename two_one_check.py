T = int(input())
for test in range(T):
    n,m = map(int, input().split())
    y = 1
    t = 2
    k = 0
    n_cp = n
    while (1):
        y_count = 0
        t_count = 0
        if (n % 2 != 0):
            while (n > 1 + k):
                n = n - t
                t_count+=1
            while (n > 0):
                n = n - y
                y_count+=1
        else:
            while (n > 0 + k):
                n = n - t
                t_count+=1
            while (n > 0):
                n = n - y
                y_count+=1
        total_count = t_count + y_count
        if (total_count == m):
            print("#{}".format(test+1), end=' ')
            print(y_count, t_count)
            break
        else:
            n = n_cp
            k+=2
