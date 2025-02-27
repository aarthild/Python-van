# cook your dish here
for _ in range(int(input())):
    n=int(input())
    time=0
    while True:
        if n==2:
            print(time+2)
            break
        elif n==1 or n==3:
            print(time+1)
            break
        else:
            time+=1
            n-=2
