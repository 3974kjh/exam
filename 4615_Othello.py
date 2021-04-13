T = int(input())
for test in range(T):
    N,M = map(int, input().split())
    array = [[0] * (N) for i in range(N)]
    check = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)) 

    fi = int(N/2)
    array[fi-1][fi-1] = 2
    array[fi][fi-1] = 1
    array[fi-1][fi] = 1
    array[fi][fi] = 2

    for i in range(M):
        r,c,o = map(int, input().split())
        r = r - 1
        c = c - 1
        array[r][c] = o

        for i in range(8):
            ar, ac = check[i]
            ch_r, ch_c = r + ar, c + ac
            change = []
            while 1:
                if ch_r < 0 or ch_c < 0 or ch_r > N - 1 or ch_c > N - 1:
                    change.clear()
                    break
                elif array[ch_r][ch_c] == 0:
                    change.clear()
                    break
                elif array[ch_r][ch_c] == o:
                    break
                else:
                    change.append((ch_r,ch_c))
                    ch_r = ch_r + ar
                    ch_c = ch_c + ac

            for rch_r, rch_c in change:
                if  o == 1:
                    array[rch_r][rch_c] = 1
                else:
                    array[rch_r][rch_c] = 2
            
    W = 0
    B = 0    
    for i in range(N):
        for j in range(N):
            if array[i][j] == 1:
                B+=1
            elif array[i][j] == 2:
                W+=1

    print("#{} {} {}".format(test+1, B, W))