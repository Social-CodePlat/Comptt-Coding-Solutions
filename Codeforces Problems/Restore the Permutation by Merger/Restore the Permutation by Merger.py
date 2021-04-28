def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
     
t=int(input())
for i in range(t):
	n=int(input())
	my_list2=[]
	my_list=[]
	arr=[int(x) for x in input().split()]
	my_list=(unique(arr))
	for i in my_list:
		my_list2.append(str(i))
	x=" ".join(my_list2)
	print(x)