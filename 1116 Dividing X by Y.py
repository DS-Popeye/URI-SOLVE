while(True):
    try:
        n = int(input())
        i = 1
        for i in range(n):
            a,b = list(map(int,input().split()))
            if(b==0):
                print("divisao impossivel")
            else:
                print("%.1f" % (a / b))

    except EOFError:
        break