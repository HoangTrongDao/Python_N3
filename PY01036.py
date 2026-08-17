import sys
try:
        t = int(input().strip())
        for _ in range(t):
            n = int(input().strip())
            tong = 0.0
            if n % 2 == 0:
                # S = 1/2 + 1/4 + 1/6 + ... + 1/N (N chẵn)
                # Vòng lặp chạy từ 2 đến N, mỗi bước nhảy 2 đơn vị
                for i in range(2, n + 1, 2):
                    tong += 1.0 / i
            else:
                # S = 1 + 1/3 + 1/5 + ... + 1/N (N lẻ)
                # Vòng lặp chạy từ 1 đến N, mỗi bước nhảy 2 đơn vị
                for i in range(1, n + 1, 2):
                    tong += 1.0 / i
            print(f"{tong:.6f}")
            
except EOFError:
        pass