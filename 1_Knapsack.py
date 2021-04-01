T = int(input())
for test in range(T):
    N,K = map(int, input().split())
    V = []
    C = []
    for i in range(N):
        n,v = map(int, input().split())
        V.append(n)
        C.append(v)
    
    def knapsack(W, v, c, N):
        K = [[0 for x in range(W+1)]for x in range(N+1)]
        for n in range(N+1):
            for w in range(W+1):
                if n==0 or w==0:
                    K[n][w] = 0
                elif v[n-1] <= w:
                    K[n][w] = max(c[n-1]+K[n-1][w-v[n-1]], K[n-1][w])
                else:
                    K[n][w] = K[n-1][w]
        return K[N][w]
    
    print("#{}".format(test+1),end=' ')
    print(knapsack(K, V, C, N))               