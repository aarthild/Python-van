# cook your dish here
for i in range(int(input())):
    x,y,z,v,u=map(int,input().split())
    if (z-x)/v > (y-z)/u:
        print("kefa")
    elif (z-x)/v < (y-z)/u:
        print("chef")
    else:
        print("draw")