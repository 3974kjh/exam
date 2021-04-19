dx, dy = [1,0,-1,0],[0,1,0,-1]
for _ in range(10):
    test = int(input())
    board = [list(input()) for _ in range(100)]
    x, y = 0, 0

    for i in range(100):
        for j in range(100):
            if board[i][j] == '2':
                x, y = i, j
                break
    flag = 0
    stack = [(x, y)]
    while stack:
        ax, ay = stack.pop()
        for i in range(4):
            kx = ax + dx[i]
            ky = ay + dy[i]
            if 0 <= kx < 100 and 0 <= ky < 100:
                if board[kx][ky] == '0':
                    stack.append((kx, ky))
                    board[kx][ky] = '1'
                elif board[kx][ky] == '3':
                    flag = 1
                    stack.clear()
                    break
    print(f"#{test} {flag}")