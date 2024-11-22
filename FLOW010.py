# cook your dish here
x=int(input())
for _ in range(x):
    a=input()
    if a=="b" or a=="B":
        print("battleship")
    elif a=='c' or a=='C':
        print("cruiser")
    elif a=='d' or a=='D':
        print("destroyer")
    else:
        print("frigate")