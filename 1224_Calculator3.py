for test in range(10):
    def calculation(k):
        x_num = []
        p_num = []
        if len(k) > 3:
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
            if len(x_num) == 0:
                x_res = 0
            tmp.append(x_res)
            cal = p_res + sum(tmp)
        
        else:
            if k[1] == '*':
                cal = int(k[0]) * int(k[2])
            else:
                cal = int(k[0]) + int(k[2])
        return str(cal)

    N = int(input())
    A = list(map(str, input()))
    if A[0] == '(':
        del(A[0])
    if A[len(A)-1] == ')':
        del(A[len(A)-1])
    res = []
    here_1 = []
    here_2 = []
    here_3 = []
    here_4 = []
    count = 0
    a = 0
    b = 0
    c = 0
    d = 0
    l = len(A)
    for i in range(l):
        if A[i] == '(':
            count+=1
        elif count == 0:
            if A[i] != ')':
                res.append(A[i])
        elif count == 1:
            if A[i] == ')':
                count-=1
                a = calculation(here_1)
                here_1.clear()
            else:
                here_1.append(A[i])
        elif count == 2:
            if A[i] == ')':
                count-=1
                b = calculation(here_2)
                here_2.clear()
            else:
                here_2.append(A[i])
        elif count == 3:
            if A[i] == ')':
                count-=1
                c = calculation(here_3)
                here_3.clear()
            else:
                here_3.append(A[i])
        elif count == 4:
            if A[i] == ')':
                count-=1
                d = calculation(here_4)
                here_4.clear()
            else:
                here_4.append(A[i])
        if int(a) > 0:
            res.append(a)
            a = 0
        if int(b) != 0:
            here_1.append(b)
            b = 0
        if int(c) > 0:
            here_2.append(c)
            c = 0
        if int(d) > 0:
            here_3.append(d)
            d = 0
    a = calculation(res)
    print("#{} {}".format(test+1, a))