

# cook your dish here

grid=int(input())
for g in range(grid):
  r,c=map(int,input().split())
  one=(r//2)*(c//2)
  print(abs((r*c)-(one*4)))
  
