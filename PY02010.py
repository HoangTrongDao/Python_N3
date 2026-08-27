while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        s = input().strip()
        s = s.lstrip('0') or '0'
        a.append(s)
    min_num = a[0]
    max_num = a[0]
    for x in a:
        if len(x) < len(min_num) or (len(x) == len(min_num) and x < min_num):
            min_num = x
        if len(x) > len(max_num) or (len(x) == len(max_num) and x > max_num):
            max_num = x
    if min_num == max_num:
        print("BANG NHAU")
    else:
        print(min_num, max_num)