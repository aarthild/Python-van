# cook your dish here
x=int(input())
for _ in range(x):
    a=int(input())
    if 2000<=a:
        print("1")
    elif 1600<=a<2000:
        print("2")
    elif a<1600:
        print("3")