t=int(input())
for i in range(t):
	n=int(input())
	arr=[int(x) for x in input().split()]
	my_list=[]
	my_list1=[]
	for j in range(len(arr)):
		summ=sum(my_list)
		summ1=sum(my_list1)
		if summ>summ1:
			a=max(arr)
			my_list1.append(a)
			arr.remove(a)
		elif summ1>summ:
			b=max(arr)
			my_list.append(b)
			arr.remove(b)
		else:
			c=max(arr)
			my_list.append(c)
			arr.remove(c)
	if sum(my_list)==sum(my_list1):
		print("YES")
	else:
		print("NO")
