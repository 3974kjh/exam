T = int(input())
for test in range(T):
    m,d=map(int, input().split())
    M = m-1
    D = d-1
    res = 0
    m_d = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(M):
        res+=m_d[i]
    res+=D
    print("#{}".format(test+1),end=' ')
    here = res%7 + 4
    if (here > 6):
        here-=7
    print(here)