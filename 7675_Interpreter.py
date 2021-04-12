T = int(input())
for test in range(T):
    end = ['.','?','!']
    N = int(input())
    n = input().split()
    cnt = []
    name = 0
    check = 0
    count = 0
    for i in range(len(n)):
        for j in range(len(n[i])):
            if j == 0:
                if 'A' <= n[i][j] and n[i][j] <= 'Z':
                    check+=1
            elif j == len(n[i])-1:
                if '.' == n[i][j] or '?' == n[i][j] or '!' == n[i][j]:
                    check+=1
                elif 'a' <= n[i][j] and n[i][j] <= 'z':
                    check+=1
            else:
                if 'a' <= n[i][j] and n[i][j] <= 'z':
                    check+=1
        if check == len(n[i]):
            count+=1
        check = 0
        for k in range(3):
            if n[i][len(n[i])-1] == end[k]:
                cnt.append(count)
                count = 0
    print("#{}".format(test+1),end=' ')         
    for i in range(len(cnt)):
        print(cnt[i], end=' ')
    print('')