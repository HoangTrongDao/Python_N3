t = int(input())
while t:
    s1 = input()
    a = []
    tg = 0
    for c in s1:
        if c.isalpha():
            a.append(c)
        else:
            tg +=int(c)
    a.sort()
    print("".join(a)+str(tg))
    t-=1