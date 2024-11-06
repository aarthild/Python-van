# cook your dish here
def count_even_odd_divisors(n):
    e = 0  # Counter for even divisors
    o = 0  # Counter for odd divisors
    for i in range(1, n + 1):
        if n % i == 0:  # Check if i is a divisor of n
            if i % 2 == 0:
                e += 1  # Count even divisor
            else:
                o += 1  # Count odd divisor
    return e, o

x = int(input())
for _ in range(x):
    a = int(input())
    e, o = count_even_odd_divisors(a)  # Get counts of even and odd divisors
    if e > o:
        print(1)
    elif e == o:
        print(0)
    else:
        print(-1)
