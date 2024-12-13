# cook your dish here
for i in range(int(input())):
    a=int(input())
    if a%4==1:
        print('east')
    elif a%4==2:
        print('south')
    elif a%4==3:
        print("west")
    else:
        print("north")
