# cook your dish here
a,b,c,d=map(int,input().split())
f=a*b*c
g=d**3
if f>g:
    print("Cuboid")
elif f==g:
    print("Equal")
else:
    print("Cube")
