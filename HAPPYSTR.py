for i in range(int(input())):
    s = input()  
    c = 0  
    happy = False 

    for char in s:
        if char in 'aeiou': 
            c += 1
            if c > 2: 
                happy = True
                break  
        else:
            c = 0 

    if happy:
        print('HAPPY')
    else:
        print('SAD')