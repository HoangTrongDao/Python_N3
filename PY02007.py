import sys
try:
    input_data = sys.stdin.read().split()
    
    a = [int(x) for x in input_data[:10]]
    a = a[:10]
    cnt = set()
    for so in a:
        so_du = so%42
        cnt.add(so_du)
    print(len(cnt))
except EOFError:
    pass