j = int(input())
for i in range (j):
    N = int(input())
    if(N>0):
        if (N % 2 == 0):
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif(N<0):
        if (N % 2 == 0):
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    else:
        print("NULL")


