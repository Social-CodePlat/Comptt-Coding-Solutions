n,k = [int(x) for x in input().split()]
list1= [int(d) for d in input().split()]

list2=[]
for i in range(len(list1)):
	list2.append(5-list1[i])
count=0
for i in range(len(list2)):
	if list2[i]>=k:
		count+=1
print(count//3)