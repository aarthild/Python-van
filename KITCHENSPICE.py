# cook your dish here
x=int(input())
for i in range(x):
    a=int(input())
    if a<4:
        print("MILD")
    elif a>=4 and a<7:
        print("MEDIUM")
    else:
        print("HOT")