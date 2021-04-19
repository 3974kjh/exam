T  = int(input())
for test in range(T):
    N = list(map(int, input().split()))
    num = N.pop(0)
    mean = sum(N) / num
    cnt = 0
    for i in N:
        if i > mean:
            cnt+=1
    res = cnt*100/num
    print('%.3f' %res,end='')
    print('%')