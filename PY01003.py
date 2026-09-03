import sys
try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        base = 10
        while n>base:
            c_s = (n%base)//(base//10)
            if c_s>=5:
                n = n + (base-(n%base))
            else:
                n = n-(n%base)
            base*=10
        print(n)

except EOFError:
    pass