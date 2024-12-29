# cook your dish here
t=int(input())
for I in range (t) :
    
    a, b, c=map(int, input().split())
    if (a==b and b==c):
        print("Yes")
     
    elif(a>=b and a>=c and (b+c+1)>=a) :
        print ("Yes")
    elif(b>=a and b>=c and (c+a+1)>=b):
        print("Yes")
    elif(c>=a and c>=b and (a+b+1)>=c):
        print("Yes")
    else:
        print("No")