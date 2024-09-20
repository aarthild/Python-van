# cook your dish here
n=int(input())
for i in range(1,n+1):
    x=int(input())
    if x<3:
        print("light")
    elif x>=3 and x<7:
        print("moderate")
    else:
        print("heavy")
