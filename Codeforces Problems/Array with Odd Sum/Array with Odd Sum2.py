t=int(input())
for i in range(t):
	n=int(input())
	arr=[int(x) for x in input().split()]
	if sum(arr)%2!=0:
		print("YES")
		continue
	else:
		for j in range(len(arr)):
			if arr[j]%2==0:
				a=j
			if arr[j]%2!=0:
				b=j
				arr[a]=arr[b]
				break
		if sum(arr)%2!=0:
			print("YES")
			print(arr)
			continue
		print("NO")