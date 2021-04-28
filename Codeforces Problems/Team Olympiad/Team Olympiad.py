n=int(input())
my_list1=[]
my_list2=[]
my_list3=[]
arr=[int(x) for x in input().split()]
for i in range(len(arr)):
	if arr[i]==1:
		my_list1.append(i+1)
	elif arr[i]==2:
		my_list2.append(i+1)
	else:
		my_list3.append(i+1)
t=min(len(my_list1),len(my_list2),len(my_list3))
print(t)
k=0
for i in range(t):
	print(my_list1[k],end=" ")
	print(my_list2[k],end=" ")
	print(my_list3[k])
	k+=1