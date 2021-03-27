print(2, end = ' ')
print(3, end = ' ')

for i in range(4, 1000000):
    k = 1
    count = 0
    if (i % 2 != 0 and i % 3 != 0):
        while (k * k <= i):
            if (i % k == 0):
                count+=1
            k+=1
        if (count == 1):
            print(i, end = ' ')