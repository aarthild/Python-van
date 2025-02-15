# cook your dish here
t=int(input())
for i in range(t):
    aar,o = map(int,input().split())
    while(o):
        aar,o = o,aar%o
    print(aar)    