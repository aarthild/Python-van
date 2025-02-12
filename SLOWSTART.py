for _ in range(int(input())):
    x,h = map(int,input().split())
    count = 0
    for i in range(1000):
        if h <=0:
            print(i)
            break
        if i <5:
            h = h - x//2
            count +=1
        else: 
            h = h-x
            count +=1 
