t=int(input())
for i in range(t):
	n,d=[int(x) for x  in input().split()]
	arr=[int(x) for x in input().split()]
	arr1=arr
	min1=min(arr1)
	arr1.remove(min1)
	min2=min(arr1)
	arr1.remove(min2)
	if max(arr)<=d:
		print('YES')
	elif min1+min2<=d:
		print("YES")
	else:
		print("NO")

