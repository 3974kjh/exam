T = int(input())
res=[]
for test in range(T):
    A = list(map(int, input().split()))
    alice = A[0]/A[1]
    bob = A[2]/A[3]
    if alice > bob:
        res.append('ALICE')
    elif alice == bob:
        res.append('DRAW')
    else:
        res.append('BOB')
for i in range(T):
    print("#{} {}".format(i+1, res[i]))