t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    # Your code goes here
    m=x*5+y*10
    print(m//z)
    t -= 1
