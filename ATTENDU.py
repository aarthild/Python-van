# cook your dish here
for i in range(int(input())):

    a = int(input())

    b = input()
    count = b.count("1")
    count+= 120-a
    if (count/120)*100>=75:
        print("YES")
    else:
        print("NO")