T = int(input())
for test in range(T):
    a, b = map(int, input().split())
    print("#{}".format(test+1), end = ' ')
    print(a+b)