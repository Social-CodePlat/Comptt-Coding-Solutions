t=int(input())
for i in range(t):
	a,b,n=[int(x) for x  in input().split()]
	count=0
	while a<=n and b<=n:
		if a==min(a,b):
			a+=max(a,b)
		elif b==min(a,b):
			b+=max(a,b)
		count+=1
	print(count)
