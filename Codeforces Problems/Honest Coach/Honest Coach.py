t=int(input())
for i in range(t):
	n=int(input())
	my_list=[]
	arr=[int(x) for x in input().split()]
	arr_sorted=sorted(arr)
	for j in range(len(arr)-1):
		my_list.append(arr_sorted[j+1]-arr_sorted[j])
	print(min(my_list))