T = int(input())
for test in range(T):
    num1, num2 = map(int, input().split())
    f = []
    s = []
    f.append(input().split())
    s.append(input().split())
    set1 = set(f[0])
    set2 = set(s[0])
    print("#{}".format(test+1), end=' ')
    print(len(set1 & set2))