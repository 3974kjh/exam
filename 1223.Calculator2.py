for test in range(10):
    N = int(input())
    k = list(map(str, input()))
    x_num = []
    p_num = []    
    for i in range(len(k)-2):
        if k[i] == '+' and k[i+2] == '+':
            if i == 1:
                p_num.append(int(k[0]))
            p_num.append(int(k[i+1]))
        elif k[i] == '+' and k[i+2] == '*':
            if i == 1:
                p_num.append(int(k[0]))
            x_num.append(int(k[i+1]))
            x_num.append(k[i+2])
        elif k[i] == '*' and k[i+2] == '+':
            if i == 1:
                x_num.append(int(k[0]))
            x_num.append(int(k[i+1]))
            x_num.append(k[i+2])
        elif k[i] == '*' and k[i+2] == '*':
            if i == 1:
                x_num.append(int(k[0]))
            x_num.append(int(k[i+1]))
            x_num.append(k[i+2])

    if k[len(k)-2] == '*':
        x_num.append(int(k[len(k)-1]))
    else:
        p_num.append(int(k[len(k)-1]))

    p_res = sum(p_num)
    x_res = 1
    tmp = []
    for i in range(len(x_num)):
        if type(x_num[i]) == int:
            x_res*=x_num[i]
        if x_num[i] == '+':
            tmp.append(x_res)
            x_res = 1
            if i == len(x_num)-1:
                x_res = 0
    tmp.append(x_res)
    res = p_res + sum(tmp)
    print("#{} {}".format(test+1,res))