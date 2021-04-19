res = [1] * 10100
for i in range(9993):
    N = i + i
    if i < 10:
        res[N] = 0
    if i >= 10:
        change = str(i)
        num = list(map(int, change))
        i+=sum(num)
        res[i] = 0
for idx in range(10101):
    if res[idx] == 1:
        print(idx)
    if idx == 9993:
        break