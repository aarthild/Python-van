
for i in range(int(input())):
    n = 4
    d = dict(input().split() for _ in range(n))
    if(d['Barcelona']>d['Eibar'] and d['RealMadrid']<d['Malaga']):
        print("Barcelona")
    else:
        print("RealMadrid")
    
    
    