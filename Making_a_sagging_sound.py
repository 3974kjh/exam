T = int(input())
for test in range(T):
    l = list(map(str, input()))
    H = int(input())
    H_n = list(map(int, input().split()))
    H_n.sort(reverse=True)
    for i in range(len(H_n)):
        l.insert(H_n[i],'-')
    print("#{}".format(test+1),end=' ')
    for i in range(len(l)-1):
        print(l[i],end='')
    print(l[len(l)-1])