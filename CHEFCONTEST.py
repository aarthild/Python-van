# cook your dish here
for i in range(int(input())):
    X,Y,A,B = map(int,input().split())
    chef = X+10*A
    chefina = Y+B*10 
    if chef > chefina :
        print("Chefina")
    elif chef == chefina: print("Draw")
    else : print("Chef")