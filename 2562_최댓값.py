N = []
for i in range(9):
    k = int(input())
    N.append(k)
M = max(N)
idx = 0
for i in range(9):
    if M == N[i]:
        idx = i
        break
print(M)
print(idx+1)