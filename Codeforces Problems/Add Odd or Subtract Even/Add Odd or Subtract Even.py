for i in range(int(input())):
	a,b=[int(x) for x in input().split()]
	if b>a:
		c=b-a
		if c%2==1:
			print(1)
		else:
			print(2)
	elif a>b:
		c=a-b
		if c%2==0:
			print(1)
		else:
			print(2)
	else:
		print(0)


