def checkstr(arm):
		count=0
		arr1=[]
		game=False
		for k in range(len(arm)):
			for m in range(k+1,len(arm)):
				arr1.append(abs(arm[k]-arm[m]))
		print(arr1)
		for i in range(len(arr1)):
			if arr1[i]>=max(arm):
				count+=1
		if count==((len(arm)*(len(arm)-1)//2)):
			game=True
		print(count)
		return game
arm=[0]
if(checkstr(arm)):
	print("yes")