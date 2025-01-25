# cook your dish here

def opposite_attract():

    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input()
        T = ''.join('1' if char == '0' else '0' for char in S)
        print(T)
opposite_attract()       
    
