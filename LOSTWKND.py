# cook your dish here

t = int(input())

for _ in range(t):
	#a1,a2,a3,a4,a5,p = map(int,input().split())
	lst =list( map(int,input().split()))
	work_hour = lst[-1] * sum(lst[0:-1])
	if (work_hour > 120):
		print("Yes")
	else:
		print("No")
	