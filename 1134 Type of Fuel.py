a = 0
b = 0
c = 0
while(True):
    n = int(input())
    if(n == 4):
        break
    elif(n == 1):
        a += 1
    elif(n == 2):
        b += 1
    elif(n == 3):
        c += 1
print("MUITO OBRIGADO")
print("Alcool:",a)
print("Gasolina:",b)
print("Diesel: ",c)