def dep(n):
    s = str(n)
    return (
        len(s) % 2 == 0
        and all(c in "02468" for c in s)
        and s == s[::-1]
    )
t = int(input())
while t:
    n = int(input())
    for i in range(1, n):
        if dep(i):
            print(i, end=" ")
    print()
    t -= 1