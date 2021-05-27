t=int(input())
for i in range(t):
	n=int(input())
	my_list=[]
	my_list2=[]
	arr=[int(x) for x in input().split()]
	for j in range((len(arr)//2)):
		my_list.append(arr[j])
		my_list.append(arr[len(arr)-1-j])
	if len(my_list)!=len(arr):
		my_list.append((arr[len(arr)//2]))
	for k in range(len(my_list)):
		my_list2.append(str(my_list[k]))
	x=' '.join(my_list2)
	print(x)