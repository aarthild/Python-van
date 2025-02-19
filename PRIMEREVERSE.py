# cook your dish here


n = int(input())

while n != 0:
    c = int(input())
    a = str(input())
    b = str(input())
    s_a = 0
    s_b = 0
    for i in a:
        s_a += int(i)
    for j in b:
        s_b += int(j)
    if s_a == s_b:
        print("YES")
    else:
        print("NO")
    n -= 1