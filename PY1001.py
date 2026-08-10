def chan_le(n):
    if n%2==0:
        return True
    else:
        return False
n = int(input())
if chan_le(n):
    print("CHAN\n")
else:
    print("LE\n")