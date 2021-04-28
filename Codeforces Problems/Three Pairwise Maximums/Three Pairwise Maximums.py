t=int(input())
for i in range(t):
	arr=[int(x) for x  in input().split()]
	max_arr,min_arr=max(arr),min(arr)
	if arr.count(max_arr)==3:
		print("YES")
		print(max_arr,max_arr,max_arr)
	elif arr.count(max_arr)==2:
		print("YES")
		print(max_arr,min_arr,min_arr)
	else:
		print("NO")
