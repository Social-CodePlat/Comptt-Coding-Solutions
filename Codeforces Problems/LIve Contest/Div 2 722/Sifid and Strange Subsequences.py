t=int(input())
for i in range(t):
	myarr=[]
	def appendinarr(elem):
		myarr.append(elem)
		return myarr
	def printSubsequences(arr, index, subarr):
		if index == len(arr):
			if len(subarr) != 0:
				appendinarr(subarr)
		else:
			printSubsequences(arr, index + 1, subarr)
			printSubsequences(arr, index + 1,
								subarr+[arr[index]])	
		return
	def checkstr(arm):
		count=0
		arr1=[]
		game=False
		for k in range(len(arm)):
			for m in range(k+1,len(arm)):
				arr1.append(abs(arm[k]-arm[m]))
		for i in range(len(arr1)):
			if arr1[i]>=max(arm):
				count+=1
		if count==((len(arm)*(len(arm)-1)//2)):
			game=True
		return game
	n=int(input())
	arr=[int(x) for x in input().split()]
	printSubsequences(arr, 0,[])
	count=0
	arr1=[]
	arr2=[]
	for j in range(len(myarr)):
		if(checkstr(myarr[j])):
			arr1.append(myarr[j])
	for q in range(len(arr1)):
		arr2.append(len(arr1[q]))
	print(max(arr2))
	