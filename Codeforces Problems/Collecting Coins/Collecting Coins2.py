t=int(input())
for i in range(t):
	a,b,c,d=[int(x) for x in input().split()]
	req=max(a,b,c)
	mid=0
	for j in a,b,c:
		mid+=req-j
	if mid<=d:
		d=d-mid
		if d%3==0:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")