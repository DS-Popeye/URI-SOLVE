N = int(input())
D = 0
for i in range(N):
    A,B = list(map(int,input().split()))
    if(A==B):
        print(0)
    else:
        C = 0
        if (A > B):
            C = A
            A = B
            B = C
            while(A < (B- 1)):
                A += 1
                if(A % 2 != 0):
                    D += A
            print(D)
