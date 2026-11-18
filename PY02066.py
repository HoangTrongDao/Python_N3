import sys
input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    a = [int(x) for x in input_data[1 : n + 1]]
    
    set_a = set(a)
    max_a = max(a)
    co_thieu_so = False
    
    for i in range(1, max_a + 1):
        if i not in set_a:
            print(i)            
            co_thieu_so = True 
    if co_thieu_so == False:
        print("Excellent!")
    