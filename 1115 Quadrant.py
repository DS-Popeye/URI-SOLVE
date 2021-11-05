while(True):
    try:
        a,b = list(map(int,input().split()))
        if(a==0 or b==0):
            break
        else:
            if(a < 0 and b >0):
                print("segundo")
            elif(a < 0 and b < 0):
                print("terceiro")
            elif( a > 0 and b < 0):
                print("quarto")
            else:
                print("primeiro")
    except EOFError:
        break