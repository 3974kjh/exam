def dfs(B_idx, O_idx, time):
 
    while len(Blue) != 0 or len(Orange) != 0:
        
        if robot_order[0] == 'B':
            
            if int(robot_order[1])-1 > B_idx:
                B_idx += 1
            elif int(robot_order[1])-1 < B_idx:
                B_idx -= 1
            else:
                robot_order.pop(0)
                robot_order.pop(0)
                Blue.pop(0)
 
            if len(Orange) != 0:
                if O_idx > Orange[0]-1:
                    O_idx -= 1
                elif O_idx < Orange[0]-1:
                    O_idx += 1
 
        else:
            if int(robot_order[1])-1 > O_idx:
                O_idx += 1
            elif int(robot_order[1])-1 < O_idx:
                O_idx -= 1
            else:
                robot_order.pop(0)
                robot_order.pop(0)
                Orange.pop(0)
 
            if len(Blue) != 0:
                if B_idx > Blue[0]-1:
                    B_idx -= 1
                elif B_idx < Blue[0]-1:
                    B_idx += 1
        time += 1
    return time
 
T = int(input())
 
for test in range(T):
    robot_order = list(map(str,input().split()))
    Blue = []
    Orange = []

    for i in range(1, len(robot_order)-1):
        if robot_order[i] == 'O':
            Orange.append(robot_order[i+1])
        elif robot_order[i] == 'B':
            Blue.append(robot_order[i+1])
    robot_order.pop(0)
    Orange = list(map(int, Orange))
    Blue = list(map(int, Blue))   
    print('#{} {}'.format(test+1,dfs(0,0,0)))