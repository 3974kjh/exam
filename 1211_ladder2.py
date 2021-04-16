for test in range(10):
    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    x_l = []
    for i in range(100):
        if arr[99][i] == 1:
            x_l.append(i)
    count_l = []
    x_idx = []
    for x in x_l:
        count = 0
        y = 99
        while True:
            if x > 0 and arr[y][x-1]:
                while x > 0 and arr[y][x-1]:
                    count+=1
                    x -= 1
                else:
                    count+=1
                    y -= 1
            elif x < 99 and arr[y][x+1]:
                while x < 99 and arr[y][x+1]:
                    count+=1
                    x += 1
                else:
                    count+=1
                    y -= 1
            else:
                count+=1
                y -= 1
            if y == 0:
                x_idx.append(x)
                count_l.append(count)
                break
    min_count = min(count_l)
    for i in range(len(count_l)):
        if min_count == count_l[i]:
            idx = i
            break
    print('#{} {}'.format(test+1, x_idx[idx]))