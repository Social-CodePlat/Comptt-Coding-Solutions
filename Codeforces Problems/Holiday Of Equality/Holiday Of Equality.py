n=int(input())
arr=[int(x) for x in input().split()]
maxnum= max(arr)
my_list=[]
for i in range(len(arr)):
	my_list.append(maxnum-arr[i])
print(sum(my_list))