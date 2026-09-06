t = int(input())
while t:
    s = input()
    res=""
    i=0
    while i<len(s):
        dem=1
        while i+1<len(s) and s[i]==s[i+1]:
            dem+=1
            i+=1
        res += str(dem) +s[i]
        i+=1

    print(res)
    t-=1