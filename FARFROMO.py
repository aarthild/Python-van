# cook your dish here
T = int(input())

for _ in range(T):
    (X1, Y1, X2, Y2) = map(int, input().split())
    Alex_distance = X1*X1 + Y1*Y1
    Bob_distance = X2*X2 + Y2*Y2
    if(Alex_distance == Bob_distance):
        print("EQUAL")
    elif Alex_distance > Bob_distance:
        print("ALEX")
    else:
        print("BOB")