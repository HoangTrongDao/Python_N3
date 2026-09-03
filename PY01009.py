import sys
try:
    s = input()
    cnt_t = 0
    cnt_h = 0
    for i in range(len(s)):
        if s[i].isupper():
            cnt_h+=1
        elif s[i].islower():
            cnt_t += 1
    if cnt_t>=cnt_h:
        print(s.lower())
    else:
        print(s.upper())
except EOFError:
    pass