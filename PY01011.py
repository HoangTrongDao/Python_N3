import sys

list_so = []
queue = ["2", "4", "6", "8"]

while queue:
    nua_dau = queue.pop(0)
    s_dx = int(nua_dau + nua_dau[::-1])

    if s_dx >= 1000000:
        continue
    list_so.append(s_dx)
    if len(nua_dau) < 3:
        for so in ["0", "2", "4", "6", "8"]:
            queue.append(nua_dau + so)

list_so.sort()
try:
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        for x in list_so:
            if x < n:
                print(x, end=" ")
            else:
                break
        print()
except EOFError:
    pass