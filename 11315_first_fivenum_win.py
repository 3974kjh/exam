T = int(input())
for test in range(T):
    N = int(input())
    board = []
    check = ((0,-1),(0,1),(1,-1),(1,0),(1,1))

    for i in range(N):
        k = list(map(str, input()))
        board.append(k)

    print("#{}".format(test+1),end=' ')
    flag = 0    
    for i in range(N):

        for j in range(N):
            
            if board[i][j] == 'o':

                for k in range(5):
                    ar, ac = check[k]
                    five_upper = 1
                    ch_i, ch_j = i + ar, j + ac
                    while 1:
                        if ch_i < 0 or ch_j < 0 or ch_i > N - 1 or ch_j > N - 1:
                            break
                        elif board[ch_i][ch_j] == '.':
                            break
                        else:
                            five_upper+=1
                            ch_i = ch_i + ar
                            ch_j = ch_j + ac

                    if five_upper >= 5:
                        flag = 1
                        print('YES')
                        break
            if flag == 1:
                break
        if flag == 1:
            break
    if flag == 0:
        print('NO')