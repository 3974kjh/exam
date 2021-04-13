T = int(input())
for test in range(T):
    N = int(input())
    if N > 1:
        if N % 2 != 0:
            a = N * (int((N - 1)/2)) + N
            c = a * 2
            b = int((N - 1)/2) * (N - 2) + N - 1 + c - a
        else:
            a = int(N/2) * (N-1) + N
            c = a * 2
            b = (N - 1) * int((N - 2)/2) + N - 1 + c - a

    else:
        a = N
        b = N
        c = a * 2
    print("#{} {} {} {}".format(test+1, a, b, c))