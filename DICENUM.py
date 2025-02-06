T=int(input())

for i in range(T):

    A1,A2,A3,B1,B2,B3=map(int,input().split())
    if A1 < A2:
        A1,A2 =A2,A1
    if A2<A3:
        A2,A3 = A3,A2
    if  A1 < A2:
        A1,A2 =A2,A1
    Y=(A1,A2,A3)
    if B1 < B2:
        B1,B2 =B2,B1
    if B2<B3:
        B2,B3 = B3,B2
    if  B1 < B2:
        B1,B2 =B2,B1
    Z=(B1,B2,B3)
    
    if Y>Z:
        print('ALICE')
    elif Z>Y:
        print('BOB')
    else:
        print("TIE".upper())
    
    
    
