# cook your dish here
for i in range(int(input())):
    a, b, c = map(int, input().split())
    if (b - a) % (2 * c) == 0:  
        print("Yes")
    else:
        print("No")