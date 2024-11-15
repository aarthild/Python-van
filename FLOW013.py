# cook your dish here
t=int(input())

for i in range(t):

    A,B,C=map(int,input().split())
    z=A+B+C
    if(z==180):
        print("YES")
    else:
        print("NO")
