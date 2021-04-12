for test in range(int(input())):
    N,A,B=map(int,input().split())
    res=[]
    C=0
    for i in range(1,N):
        R=i
        C+=1
        res.append(A*abs(R-C)+B*abs(N-R*C))
        
        while (R+1)*(C+1) > N:
            C-=1
     
    print("#{}".format(test+1),end=' ')
    print(min(res))