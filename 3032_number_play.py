T = int(input())
def Euclidean(a, b):
    r1,r2 = a, b
    s1,s2 = 1, 0
    t1,t2 = 0, 1

    while(r2 > 0):
        q = r1 // r2
        r = r1 - q * r2
        r1,r2 = r2,r
 
        s = s1 - q * s2
        s1,s2 = s2,s
 
        t = t1 - q * t2
        t1,t2 = t2,t
    if r1 == 1:
        print(s1, t1)
    else:
        print(-1)

for test in range(T):
    x,y = map(int, input().split())
    a = x
    b = y
    print("#{}".format(test+1),end=' ')
    Euclidean(a, b)
