n=int(input())
arr=[int(x) for x in input().split()]
my_list2=[]
my_list2.append(arr[0])
count=0
for i in arr:
	if ((i > max(my_list2)) or (i < min(my_list2))):
		count+=1
	my_list2.append(i)
print(count)