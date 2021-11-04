N = int(input())
C = 0
for i in range(N):
    A,B = list(map(int,input().split()))
    if(A==B):
        print(C)
    elif(A<B):
        print(C+1)