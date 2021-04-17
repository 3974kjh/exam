T = int(input())
for test in range(T):
    K = int(input())
    s = list(map(str, input()))
    here = []
    for i in range(len(s)):
        k = s[i]
        here.append(k)
        for j in range(i+1, len(s)):
            k+=s[j]
            here.append(k)
    here.sort()
    l = len(here)
    idx = 0
    print("#{}".format(test+1),end=' ')
    for i in range(l-1):
        if here[idx] == here[idx+1]:
            del(here[idx+1])
        else:
            idx+=1
    if len(here) < K:
        print('none')
    else:
        print(here[K-1])