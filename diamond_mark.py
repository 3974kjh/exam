T = int(input())
for test in range(T):
    n = list(map(str, input()))
    l = len(n) * 3 + 2 + (len(n) - 1)
    for i in range(5):
        k = 2
        m = 0
        u = 2
        kk = 0
        for j in range(l):
            if ((i == 0 or i == 4) and j == k):
                print('#', end='')
                k+=4
            elif ((i == 1 or i == 3) and j % 2 == 1):
                print('#', end='')
            elif (i == 2):
                if (j == kk):
                    if (j == l - 1):
                        print('#')
                        break
                    else:
                        print('#',end='')
                    kk+=4
                elif (j == u):
                    u+=4
                    print(n[m],end='')
                    m+=1
                else:
                    print('.',end='')
            else:
                if (j == l - 1):
                    print('.')
                    break
                else:
                    print('.', end='')