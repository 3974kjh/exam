T = int(input())
for test in range(T):
    A,B = map(int, input().split())
    num = 1
    A_num = 0
    B_num = 0
    k = int(A / B)
    res = k * k
    print("#{}".format(test + 1), end=' ')
    print(res)