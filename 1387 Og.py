while(True):
    try:
        a,b = list(map(int,input().split()))
        if(a == 0 and b == 0):
            break
        else:
            c = (a + b)
            print(c)
    except EOFError:
        break