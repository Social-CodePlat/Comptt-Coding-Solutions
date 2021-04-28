t=int(input())
for i in range(t):
	a,b=[int(x) for x in input().split()]
	if a==1:
		print(0)
	elif a==2:
		print(b)
	else:
		print(2*b)
