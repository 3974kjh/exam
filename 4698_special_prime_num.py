prime = [2] 
visited = [0]*1000001
for q in range(3,1000001,2):
    if visited[q] == 0:
        prime.append(q)
        for w in range(q,1000001,q):
            if w%q == 0:
                visited[w] = 1
T = int(input())
for test in range(T):
    D,A,B = map(int, input().split())
    D = str(D)
    res = 0
    for i in prime:
        if i > B:
            break
        if i < A:
            continue
        if D in str(i):
            res+=1
        
    print("#{} {}".format(test+1, res))