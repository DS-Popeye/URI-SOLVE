a = int(input())
b = int(input())

if(a > b):
    t = a
    a = b
    b = t
    print(a,b)
while(a < b):
    a = a + 1
    if(a%5 == 2 or a%5 == 3 and a != b):
        print(a)
