T = int(input())
for test in range(T):
    A,B = map(int, input().split())
    i = 0
    k = 0
    count = 0
    while (A > k):
        i+=1
        k = i*i
    while (A <= k and k <= B):
        check = []
        i_cp = i
        while i_cp >= 10:
            check.append(i_cp%10)
            i_cp = int(i_cp / 10)
        check.append(i_cp)
        if check[0] == check[len(check)-1]:
            if i > 10 or i == 1 or i == 2 or i == 3:
                count+=1
        i+=1
        k = i*i
    print("#{}".format(test+1),end=' ')
    print(count)