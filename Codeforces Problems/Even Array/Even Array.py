t=int(input())
for i in range(t):
	n=int(input())
	even=0
	odd=0
	arr=[int(x) for x in input().split()]
	for i in range(len(arr)):
		if i%2==0 and arr[i]%2!=0:
			odd+=1
		if i%2==1 and arr[i]%2!=1:
			even+=1
	if even!=odd:
			print(-1)
	else:
		print(even)
	
	

