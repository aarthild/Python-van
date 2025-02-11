# cook your dish here
t = int(input())

for _ in range(t):

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    protein_stock = 0
    day = 0
    for i in range(n):
        total_protein = protein_stock + a[i]
        if total_protein < k:
            print("NO", i + 1)
            break
        else:
            protein_stock = total_protein - k
    else:
        print("YES")