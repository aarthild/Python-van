t = int(input())

while t > 0:
    n, x = map(int, input().split())
    # Your code goes here
    if n*x>9999 and n*x<100000:
        print("yes")
    else:
        print("no")
    t -= 1
