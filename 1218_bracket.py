for test in range(10):
    N = int(input())
    bracket = list(map(str, input()))

    here = []
    flag = 0
    print("#{}".format(test+1),end=' ')
    for i in bracket:
        if i == '(':
            here.append(1)
        elif i == '{':
            here.append(2)
        elif i == '[':
            here.append(3)
        elif i == '<':
            here.append(4)
        else:
            if here[len(here)-1] == 1 and i == ')':
                del(here[len(here)-1])
            elif here[len(here)-1] == 2 and i == '}':
                del(here[len(here)-1])
            elif here[len(here)-1] == 3 and i == ']':
                del(here[len(here)-1])
            elif here[len(here)-1] == 4 and i == '>':
                del(here[len(here)-1])
            else:
                print(0)
                flag = 1
                break
    if flag == 0:
        print(1)