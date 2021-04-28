t=int(input())
for i in range(t):
	x,y,n=[int(x) for x in input().split()]
	midans=((n-y)//x)
	ans=midans*x+y
	print(ans) 