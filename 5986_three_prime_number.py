# 실행시간 초과
T = int(input())
for test in range(T):
    N = int(input())
    prime_num = [2,3]
    for i in range(4,N):
        k = 1
        count = 0
        while k*k <= i:
            if i % k == 0:
                count+=1
            k+=1
        if count == 1:
            prime_num.append(i)
    res = [2,2,2]
    find = 0
    idx_0 = 0
    idx_1 = 0
    idx_2 = 0
    while res[0] * 3 <= N:
        while sum(res) <= N:
            while sum(res) <= N:
                res[2] = prime_num[idx_2]
                if sum(res) == N:
                    find+=1
                    break
                idx_2+=1
                if idx_2 == len(prime_num):
                    break
            idx_1+=1
            idx_2 = idx_1
            res[1] = prime_num[idx_1]
            res[2] = prime_num[idx_2]
        idx_0+=1
        idx_1 = idx_0
        idx_2 = idx_1
        res[0] = prime_num[idx_0]
        res[1] = prime_num[idx_1]
        res[2] = prime_num[idx_2]
    print("#{} {}".format(test+1, find))

#수정 -> 같은 소수를 2개이상 더했을 때 소수가 안 나오므로 2개만 고려
T = int(input())
for test in range(T):
    N = int(input())
    prime_num = [2,3]
    for i in range(4,N):
        k = 1
        count = 0
        while k*k <= i:
            if i % k == 0:
                count+=1
            k+=1
        if count == 1:
            prime_num.append(i)
    res = [2,2,2]
    find = 0
    for i in range(len(prime_num)):
        for j in range(i, len(prime_num)):
            if N - (prime_num[i] + prime_num[j]) in prime_num[j:]:
                find+=1
    print("#{} {}".format(test+1, find))