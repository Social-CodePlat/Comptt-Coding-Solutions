arr=[int(x) for x in input().split()]
maxn=max(arr)
arr.remove(maxn)
narr=[]
for i in arr:
	narr.append(maxn-i)
for i in narr:
	print(i,end=" ")