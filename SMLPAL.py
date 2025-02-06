# cook your dish here

def smallest_palindrome(X, Y):

    # Half the ones and half the twos
    half_ones = X // 2
    half_twos = Y // 2
    
    # Create the first half of the palindrome
    first_half = '1' * half_ones + '2' * half_twos
    
    # The second half is a mirror of the first half
    second_half = first_half[::-1]
    
    # Combine the two halves to form the palindrome
    return first_half + second_half

# Input reading
T = int(input())  # Number of test cases
for _ in range(T):
    X, Y = map(int, input().split())
    # Output the result for each test case
    print(smallest_palindrome(X, Y))
