T = int(input())
for test in range(T):
    H,W = map(int, input().split())
    field = []
    k = []
    for i in range(H):
        k = list(map(str, input()))
        field.append(k)
    field_item = ['^','v','<','>']
    tank_location = []
    for i in range(H):
        for j in range(W):
            for k in range(4):
                if field[i][j] == field_item[k]:
                    tank_location.append(i)
                    tank_location.append(j)
                    break
            if len(tank_location) > 1:
                break
        if len(tank_location) > 1:
            break
    move = int(input())
    move_how = list(map(str, input()))
    i_idx = tank_location[0]
    j_idx = tank_location[1]
    for i in range(move):
        if move_how[i] == 'S':
            n = 1
            if field[i_idx][j_idx] == '^':
                while (field[i_idx][j_idx] == '^' and i_idx - n >= 0):
                    if field[i_idx - n][j_idx] == '#':
                        break
                    elif field[i_idx - n][j_idx] == '*':
                        field[i_idx - n][j_idx] = '.'
                        break
                    elif field[i_idx - n][j_idx] == '-' or field[i_idx - n][j_idx] == '.':
                        n+=1
            elif field[i_idx][j_idx] == 'v':
                while (field[i_idx][j_idx] == 'v' and i_idx + n < H):
                    if field[i_idx + n][j_idx] == '#':
                        break
                    elif field[i_idx + n][j_idx] == '*':
                        field[i_idx + n][j_idx] = '.'
                        break
                    elif field[i_idx + n][j_idx] == '-' or field[i_idx + n][j_idx] == '.':
                        n+=1
                    
            elif field[i_idx][j_idx] == '<':
                while (field[i_idx][j_idx] == '<' and j_idx - n >= 0):
                    if field[i_idx][j_idx - n] == '#':
                        break
                    elif field[i_idx][j_idx - n] == '*':
                        field[i_idx][j_idx - n] = '.'
                        break
                    elif field[i_idx][j_idx - n] == '-' or field[i_idx][j_idx - n] == '.':
                        n+=1
                    
            elif field[i_idx][j_idx] == '>':
                while (field[i_idx][j_idx] == '>' and j_idx + n < W):
                    if field[i_idx][j_idx + n] == '#':
                        break
                    elif field[i_idx][j_idx + n] == '*':
                        field[i_idx][j_idx + n] = '.'
                        break
                    elif field[i_idx][j_idx + n] == '-' or field[i_idx][j_idx + n] == '.':
                        n+=1
                    
        elif move_how[i] == 'U':
            field[i_idx][j_idx] = '^'
            if i_idx - 1 >= 0:
                if field[i_idx - 1][j_idx] == '.':
                    field[i_idx][j_idx] = '.'
                    field[i_idx - 1][j_idx] = '^'
                    i_idx-=1            
        elif move_how[i] == 'D':
            field[i_idx][j_idx] = 'v'
            if i_idx + 1 < H:
                if field[i_idx + 1][j_idx] == '.':
                    field[i_idx][j_idx] = '.'
                    field[i_idx + 1][j_idx] = 'v'
                    i_idx+=1
        elif move_how[i] == 'L':
            field[i_idx][j_idx] = '<'
            if j_idx - 1 >= 0:
                if field[i_idx][j_idx - 1] == '.':
                    field[i_idx][j_idx] = '.'
                    field[i_idx][j_idx - 1] = '<'
                    j_idx-=1
        elif move_how[i] == 'R':
            field[i_idx][j_idx] = '>'
            if j_idx + 1 < W:
                if field[i_idx][j_idx + 1] == '.':
                    field[i_idx][j_idx] = '.'
                    field[i_idx][j_idx + 1] = '>'
                    j_idx+=1
    print("#{}".format(test+1),end=' ')
    for i in range(H):
        for j in range(W):
            print(field[i][j],end='')
            if j == W-1:
                print('')