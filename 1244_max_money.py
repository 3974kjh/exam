T = int(input())
for test in range(T):
    n,c = map(str, input().split())
    n = list(n)
    c = int(c)
    res = 0
    l = len(n)
    k = 0
    def dfs(k, count):
        global res
        if count == c:
            res = max(int("".join(n)), res)
            return
        for i in range(k, l):
            for j in range(i+1, l):
                if n[i] <= n[j]:
                    n[i],n[j] = n[j],n[i]
                    dfs(i, count+1)
                    n[i],n[j] = n[j],n[i]
    dfs(0,0)
    cnt = 1
    for i in range(l-1):
        if n[i] > n[i+1]:
            cnt+=1
    if l == 2 or cnt == l:
        for i in range(c):
            n[-1],n[-2] = n[-2],n[-1]
        res = int("".join(n))
    print("#{} {}".format(test+1, res))