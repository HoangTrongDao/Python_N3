def lai_suat(n,x,m):
    nam = 0
    while(n<m):
        tong =n*(x/100)
        n+=tong
        nam +=1
    return nam
# Đọc dòng đầu tiên làm số lượng bộ test
try:
    so_bo_test = int(input().strip())
    # Duyệt đúng số bộ test đề bài cho
    for _ in range(so_bo_test):
        n, x, m = map(float, input().split())
        print(lai_suat(n, x, m))
except EOFError:
    pass

