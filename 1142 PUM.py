while(True):
    try:
        n = int(input())
        count = 0
        a,b,c = 1,2,3
        for i in range(n):
            print('{0} {1} {2} PUM'.format(a,b,c))
            c = c+2
            a = c
            b = c

            b+= 1
            c+= 2
            count += 1

    except EOFError:
        break