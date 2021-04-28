t=int(input())
for i in range(t):
	n,m=[int(x) for x in input().split()]
	req=n*m
	if req%2==0:
		print(req//2)
	else:
		print((req//2)+1)