T = int(input())
for test in range(T):
    res = list(map(str, input()))
    cnt = 0
    final = 0
    for i in res:
        if i == 'O':
           cnt+=1
           final+=cnt
        elif i == 'X':
            cnt = 0
    print(final)