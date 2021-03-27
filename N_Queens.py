T=int(input())
for test in range(T):
    num = int(input())
    g_count = 0
    def check_Queen(matrix, c):
        i = 0
        while i < c:
            if(matrix[i] == matrix[c]):
                return 0
            if(abs(matrix[i] - matrix[c]) == abs(i - c)):
                return 0
            i+=1
        return 1
    
    def ft_N_Queen(matrix, num, c):
        r = 0
        if(c == num):
            global g_count
            g_count+=1
        else:
            while r < num:
                matrix[c] = r
                if(check_Queen(matrix, c)):
                    ft_N_Queen(matrix, num, c + 1)
                r+=1
    col = 0
    matrix = [0,0,0,0,0,0,0,0,0,0]
    ft_N_Queen(matrix, num, col)
    print("#{}".format(test+1),end=' ')
    print(g_count)