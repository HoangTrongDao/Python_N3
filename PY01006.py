t = int(input())

while t:
    n = input()

    if all(c == '4' or c == '7' for c in n):
        print("YES")
    else:
        print("NO")

    t -= 1