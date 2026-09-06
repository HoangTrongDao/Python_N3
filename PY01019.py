t = int(input())

while t:
    s1 = input()
    s2 = s1[::-1]

    kq = True

    for i in range(1, len(s1)):
        a = abs(ord(s1[i]) - ord(s1[i - 1]))
        b = abs(ord(s2[i]) - ord(s2[i - 1]))

        if a != b:
            kq = False
            break

    if kq:
        print("YES")
    else:
        print("NO")

    t -= 1