N = int(input())
n = list(map(int, input().split()))
res = max(n)
new = []
for i in n:
    new.append(i/res*100)
rres = sum(new) / N
print(rres)