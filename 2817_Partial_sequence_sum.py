T = int(input())

def sol(idx, sum):
    global count
    if idx >= N:
        return
    tmp = sum + A[idx]
    if tmp == K:
        count+=1
    sol(idx + 1, sum)
    sol(idx + 1, tmp)

for test in range(T):
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    sol(0, 0)
    print("#{} {}".format(test+1, count))