t = int(input())

while t > 0:
    a,b = map(int, input().split())
    # Your code goes here
    if a>=b:
        print(b*1)
    else:
        print(a+(b-a)*2)
    t -= 1
