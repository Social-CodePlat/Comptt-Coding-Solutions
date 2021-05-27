t=int(input())
for i in range(t):
	n=int(input())
	arr=[]
	arr1=[]
	arr.append(1)
	for i in range(n-1):
		arr.append(1)
	for i in range(len(arr)):
		arr1.append(str(arr[i]))
	x=" ".join(arr1)
	print(x)