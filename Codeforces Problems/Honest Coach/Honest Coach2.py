t=int(input())
for j in range(t):
	diff=10**20
	n=int(input())
	my_list=[]
	arr=[int(x) for x in input().split()]
	arr_sorted=sorted(arr)
	for i in range(len(arr_sorted)-1):
		if arr_sorted[i + 1] - arr_sorted[i] < diff:
			diff = abs(arr_sorted[i + 1] - arr_sorted[i])
	print(diff)