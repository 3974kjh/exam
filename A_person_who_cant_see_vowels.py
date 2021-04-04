T = int(input())
for test in range(T):
    a = list(map(str, input()))
    b = ['a','e','i','o','u']
    i = 0
    while (i < len(a)):
        for j in range(len(b)):
            if (a[i] == b[j]):
                del(a[i])
                i-=1
                break
        i+=1
    
    print("#{}".format(test+1),end=' ')
    for i in range(len(a)-1):
        print(a[i],end='')
    print(a[len(a)-1])