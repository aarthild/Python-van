# cook your dish here
x=int(input())
for _ in range(x):
    if x%4==0:
        print(x+1)
        break
    else:
        print(x-1)
        break
