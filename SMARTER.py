
# cook your dish here
import math
t = int(input())

for _ in range(t):
    l, v1, v2 = map(int, input().split())
    t1=l/v1
    t2=l/v2
    Haretime=math.ceil(t1)
    TortTime=math.ceil(t2)
   
        
    if Haretime==TortTime:
        print(-1)
    else:
        print(round(Haretime-TortTime-1))
        
    
