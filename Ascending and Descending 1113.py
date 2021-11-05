while(True):
    try:
        a,b = list(map(int,input().split()))
        if(a==b):
            break
        elif(a<b):
            print("Assending")
        else:
            print("Decrescente")
    except EOFError:
        break