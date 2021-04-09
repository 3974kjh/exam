T = int(input())
for test in range(T):
    n = list(map(int, input()))
    count = n[0]
    need = 0
    for i in range(1, len(n)):
        if i > count:
            need+=i - count
            count+=i - count
        if n[i] > 0:
            count+=n[i]
    print("#{} {}".format(test+1,need))