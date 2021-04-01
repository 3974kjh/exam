T = int(input())
for test in range(T):
    a = input().split()
    set1 = list(a[0])
    set2 = list(a[1])
    s1_L = len(set1)
    s2_L = len(set2)

    K = [[0 for x in range(s1_L+1)]for x in range(s2_L+1)]
    for i in range(s2_L + 1):
        for j in range(s1_L + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif set1[j-1] == set2[i-1]:
                K[i][j] = K[i-1][j-1] + 1
            else:
                K[i][j] = max(K[i][j-1], K[i-1][j])

    print("#{}".format(test+1), end= ' ')
    print(K[s2_L][s1_L])