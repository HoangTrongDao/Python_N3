import sys
s = sys.stdin.read()
cau="" 
for c in s:
    if c in ".?!":
        cau = cau.strip()
        if cau:
            cau = " ".join(cau.split())
            cau = cau.lower()
            cau = cau[0].upper()+cau[1:]
            print(cau)
        cau=" " 
    else:
        cau+=c