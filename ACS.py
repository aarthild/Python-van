# cook your dish here
t=int(input())

for _ in range(t):
    p=int(input())
    h=p//100
    one=p%100
    if((h+one)<=10):
        print(h+one)
    else:
        print(-1)
