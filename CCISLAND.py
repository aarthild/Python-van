# cook your dish here
for i in range(int(input())):
    a,b,c,d,e=map(int,input().split())
    f=a//c 
    g=b//d 
    mi=min(f,g)
    if mi>=e:
        print('yes')
    else:
        print('no')
