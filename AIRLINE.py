# cook your dish here

for _  in range(int(input())):

    a,b,c,d,e = map(int,input().split(" "))
    min_weight = min(a,b,c)
    max_weight = max(a,b,c)
    
    if ((a+b)<=d and c<=e) or ((a+c)<=d and b<=e) or ((b+c)<=d and a<=e):
        print("yes")
    else:
        print("no")