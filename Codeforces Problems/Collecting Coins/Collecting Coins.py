for i in range(int(input())):
	a,b,c,d=[int(x) for x in input().split()]
	req=max(a,b,c)
	mid=0
	mid+=req-a
	mid+=req-b
	mid+=req-c
	if mid<=d:
		d=d-mid
		if d%3==0:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")