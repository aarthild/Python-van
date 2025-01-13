# cook your dish here
while True:

    n = int(input())

    if n == 0:
        break 
    
    per = list(map(int,input().split()))
    is_ambigous = True
    for i in range(n):
        if per[per[i] - 1] != i + 1:
            is_ambigous = False
            break
        
    if is_ambigous:
        print("ambiguous")
    else:
        print("not ambiguous")
