T = int(input())

def sol(idx, sum, here):
    global sum_max
    if idx >= N:
        return
    tmp = sum + cal[idx]
    res = here + sc[idx]
    if tmp <= L:
        if res >= sum_max:
            sum_max = res
    sol(idx + 1, sum, here)
    sol(idx + 1, tmp, res)

for test in range(T):
    N,L = map(int, input().split())
    sc = []
    cal = []
    for put in range(N):
        t,k = map(int, input().split())
        sc.append(t)
        cal.append(k)
    sum_max = 0
    sol(0, 0, 0)
    print("#{} {}".format(test+1, sum_max))