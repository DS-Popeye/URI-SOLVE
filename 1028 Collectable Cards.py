import math

def mdc(num1, num2):
    resto = None
    while resto is not 0:
        resto = num1 % num2
        num1 = num2
        num2 = resto

    return num1

def mdc2(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


lista = []
n = int(input())
for i in range(n):
    x, y = [int(z) for z in input().split()]
    #lista.append(mdc(x, y))
    lista.append(mdc2(x, y))
    #lista.append(math.gcd(x,y))

for item in lista:
    print(item)