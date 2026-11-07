while True:
    try:
        a = input()
        if a == 'q':
            break  
        b = input()
        if b == 'q':
            break      
        ans = int(a) / int(b)     
    except EOFError:
        break
    except ZeroDivisionError:
        print("k chia het 0")
    except ValueError:
        print("kou")
    else:
        print(ans)