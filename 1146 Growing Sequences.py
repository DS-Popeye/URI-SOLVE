while(True):
    try:
        n = int(input())
        j = 1

        if(n <= 0):
            break
        else:
            for i in range(n):
                if  j == n:
                    print('%d' % (j), end="\n")
                else:
                    print('%d' % (j), end=" ")
                j += 1

    except EOFError:
        break