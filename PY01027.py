n = input().strip()
check = True
for char  in n:
    if char !='6' and char !='8':
        check = False
        break
if check  and len(n)>0 and n[0]=='6' and '888' not in n:
    print("YES")
else:
    print("NO")