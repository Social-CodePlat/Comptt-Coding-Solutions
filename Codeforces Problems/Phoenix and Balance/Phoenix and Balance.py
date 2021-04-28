t=int(input())
for i in range(t):
	my_list=[]
	my_list1=[]
	my_list2=[]
	summ=0
	summ1=0
	n=int(input())
	for i in range(1,n+1):
		my_list.append(2**i)
	my_list1.append(max(my_list))
	my_list.remove(max(my_list))
	my_list2.append(max(my_list))
	my_list.remove(max(my_list))
	while ((my_list1>my_list2) and (len(my_list1)!=n/2) and (len(my_list2)!=n/2)):
		my_list2.append(max(my_list))
		my_list.remove(max(my_list))
	mid=sum(my_list)
	mid2=sum(my_list1)
	print(abs((sum(my_list2)-(mid+mid2))))