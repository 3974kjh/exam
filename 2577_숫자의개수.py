N = []
for i in range(3):
    k = int(input())
    N.append(k)
res = 1
for i in N:
    res*=i
here = str(res)
print(here.count('0'))
print(here.count('1'))
print(here.count('2'))
print(here.count('3'))
print(here.count('4'))
print(here.count('5'))
print(here.count('6'))
print(here.count('7'))
print(here.count('8'))
print(here.count('9'))