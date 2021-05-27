t=int(input())
for i in range(t):
	n=int(input())
	arr=[int(x) for x in input().split()]
	my_list=[]
	my_list1=[]
	for j in range(len(arr)):
		c_count=arr.count(arr[j])
		my_list.append(arr[j])
		my_list1.append(c_count)
	mid= min(my_list1)
	req=(my_list1.index(mid))
	req1=my_list[req]
	for k in range(len(arr)):
		if arr[k]==req1:
			print(k+1)
			break