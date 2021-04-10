T = int(input())
for test in range(T):
    D,L,N = map(int,input().split())
    damage = 0
    for i in range(N):
        damage+= D * (1 + (i * L * 0.01))
    print("#{}".format(test+1),end=' ')
    print("%d" %damage)