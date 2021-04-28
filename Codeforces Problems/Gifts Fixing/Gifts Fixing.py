t=int(input())
for i in range(t):
	n=int(input())
	arr_a=[0]*n
	arr_b=[0]*n
	arr_a=[int(x) for x in input().split()]
	arr_b=[int(x) for x in input().split()]
	arr_a_min=min(arr_a)
	arr_b_min=min(arr_b)
	ans=0
	for i in range(n):
		if arr_b[i] != arr_b_min and arr_a[i] == arr_a_min:
			ans += (arr_b[i] - arr_b_min)
		if arr_b[i] == arr_b_min and arr_a[i] != arr_a_min:
			ans += (arr_a[i] - arr_a_min)
		if arr_b[i] != arr_b_min and arr_a[i] != arr_a_min:
			ans += max(arr_a[i] - arr_a_min, arr_b[i] - arr_b_min)
	print(ans)