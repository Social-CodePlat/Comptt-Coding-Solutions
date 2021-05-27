t=int(input())
for i in range(t):
	n,x= [int(k) for k  in input().split()]
	k=2
	count=1
	while k<n:
		k=k+x
		count+=1
	print(count)

