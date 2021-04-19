h, m = map(int, input().split())
if h == 0 and m < 45:
    h = 23
    m+=60 - 45
elif h == 0 and m >= 45:
    m-=45
elif h > 0 and m < 45:
    h-=1
    m+=60 - 45
elif h > 0 and m >= 45:
    m-=45
print(h, m)