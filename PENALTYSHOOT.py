# cook your dish here



for _ in range(int(input())):

    x, y = map(int, input().split())
    if x==y:
        print("yes")
    elif x>y:
        if y+1<x:
            print("no")
        else:
            print('yes')
    else:
        if x+2<y:
            print('no')
        else:
            print('yes')
    
