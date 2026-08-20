import sys
try:
    s = sys.stdin.read().split()

    for word in s:
        print(word)
except EOFError:
    pass