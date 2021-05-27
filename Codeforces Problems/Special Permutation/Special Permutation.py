import random
t=int(input())
for i in range(t):
	n=int(input())
	my_list=[]
	my_list1=[]
	my_list2=[]
	for i in range(1,n+1):
		my_list.append(i)
	my_list1=my_list[1::]
	my_list1.append(my_list[0])
	for i in range(len(my_list1)):
		my_list2.append(str(my_list1[i]))
	x=" ".join(my_list2)
	print(x)