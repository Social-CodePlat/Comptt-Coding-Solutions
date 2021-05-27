t=int(input())
for i in range(t):
	w,h,n=[int(x) for x in input().split()]
	count=1
	while w%2==0 or h%2==0:
		if w%2==0:
			w=w//2
			count*=2
		elif h%2==0:
			h=h//2
			count*=2
	if n<=count:
		print("YES")
	else:
		print("NO")

