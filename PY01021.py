try:
    t = int(input())
    for _ in range(t):
        s = input()
        a = []
        tong = 0
        for c in s:
            if(c.isdigit()):
                tong += int(c)
            else:
                a.append(c)
        a.sort()
        chuoi_cs="".join(a)
        print(f"{chuoi_cs}{tong}")

except EOFError:
    pass