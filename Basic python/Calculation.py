def sum(x,y):
    while y:
        x,y=y,x % y
    print(y,x)

sum(100,240)