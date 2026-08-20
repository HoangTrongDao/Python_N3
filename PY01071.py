import sys
try:
    s = input()
    ket_qua = s[-3:].lower()
    if ket_qua ==".py":
        print("yes\n")
    else:
        print("no\n")
except EOFError:
    pass    