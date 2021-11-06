while (True):
    try:
        n = int(input())
        a,b,c = 1,1,1
        for i in range(n):
            print('{0} {1} {2}'.format(a,b,c))
            a = a+1
            b = a*a
            c = a*b
    except EOFError:
        break