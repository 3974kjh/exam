for test in range(10):
    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if arr[99][i] == 2:
            x = i
            break
    y = 99
    while True:
        if x > 0 and arr[y][x-1]:
            while x > 0 and arr[y][x-1]:
                x -= 1
            else:
                y -= 1
        elif x < 99 and arr[y][x+1]:
            while x < 99 and arr[y][x+1]:
                x += 1
            else:
                y -= 1
        else:
            y -= 1
        if y == 0:
            break
    print('#{} {}'.format(test+1,x))