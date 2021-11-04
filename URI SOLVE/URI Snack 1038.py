X,Y = list(map(int,input().split()))
if(X == 1):
    Price = (float) (4.00 * Y)
elif(X == 2):
    Price = (float) (4.50 * Y)
elif (X == 3):
    Price = (float)(5.00 * Y)
elif(X == 4):
    Price = (float) (2.00 * Y)
elif(X == 5):
    Price = (float) (1.50 * Y)
print("Total: R$ %.2f"%Price)