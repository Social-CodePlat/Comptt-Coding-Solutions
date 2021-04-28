n=int(input())
if n%2==0:
	line1=n//2
	print(line1)
	for i in range(line1):
		print(2, end=" ")
else:
	line1=n//2 
	print(line1)
	for i in range(line1-1):
		print(2, end=" ")
	print(3,end=" ")