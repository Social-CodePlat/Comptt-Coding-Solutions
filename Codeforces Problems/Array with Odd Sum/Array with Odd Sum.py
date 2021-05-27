t=int(input())
for i in range(t):
	n=int(input())
	arr=[int(x) for x in input().split()]
	if sum(arr)%2!=0:
		print("YES")
		continue
	else:
		a=False
		b=False
		for j in range(len(arr)):
			if arr[j]%2==0:
				a=True
			if arr[j]%2!=0:
				b=True
		if a and b:
			print("YES")
			continue
		print("NO")
