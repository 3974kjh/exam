N = []
for i in range(10):
    k = int(input())
    N.append(k)
res = []
for i in N:
    res.append(i%42)
res.sort()
cnt = 1
for i in range(9):
    if res[i] != res[i+1]:
        cnt+=1
print(cnt)