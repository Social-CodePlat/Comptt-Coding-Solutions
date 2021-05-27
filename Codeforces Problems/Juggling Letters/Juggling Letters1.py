t=int(input())
def countlet(strn,let,count):
	for i in strn:
		if i==let:
			count+=1
	return count
for i in range(t):
	n=int(input())
	arr=[]
	arr1=[]
	arr2=[]
	for j in range(n):
		strn=input()
		arr.append(strn)
		for k in strn:
			if k in arr1:
				continue
			else:
				arr1.append(k)
	for l in arr1:
		count=0
		for w in arr:
			count=int(countlet(w,l,count))
		arr2.append(count)
	game=True
	for m in arr2:
		if m%n !=0:
			game=False
			break
		else:
			continue
	print("YES" if game else "NO")