T = int(input())
for test in range(T):
    n = list(map(str, input()))
    bf_e = []
    for i in range(len(n)):
        if 'A' <= n[i] and n[i] <= 'Z':
            here = ord(n[i])-65
        elif 'a' <= n[i] and n[i] <= 'z':
            here = ord(n[i])-71
        elif '0' <= n[i] and n[i] <= '9':
            here = ord(n[i])+4
        elif n[i] == '/' or n[i] == '+':
            if n[i] == '/':
                here = ord(n[i])+16
            else:
                here = ord(n[i])+19
        six=[]
        for i in range(6):
            six.append(here%2)
            here = int(here / 2)
        six.reverse()
        bf_e.extend(six)
    af_d = []
    res = 0
    for i in range(len(bf_e)):
        res = res*2 + bf_e[i] 
        if ((i + 1) % 8 == 0):
            af_d.append(res)
            res = 0
    print("#{}".format(test+1),end =' ')
    for i in range(len(af_d)-1):
        print('%c' %af_d[i],end='')
    print('%c' %af_d[len(af_d)-1])