T = int(input())
for test in range(T):
    score = list(map(int, input().split()))
    for i in range(len(score)):
        if score[i] < 40:
            score[i] = 40
    print("#{}".format(test+1), end=' ')
    print(int(sum(score) / len(score)))