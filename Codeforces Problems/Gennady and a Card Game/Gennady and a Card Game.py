s1=input()
arr=[str(x) for x in input().split()]
arr1=[]
arr2=[]
for i in range(len(arr)):
	arr1.append(arr[i][0])
for i in range(len(arr)):
	arr2.append(arr[i][1])
if (s1[0] in arr1) or (s1[1] in arr2):
	print("YES")
else:
	print("NO")