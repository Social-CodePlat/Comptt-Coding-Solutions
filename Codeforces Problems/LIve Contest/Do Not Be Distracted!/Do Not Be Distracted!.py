t=int(input())
for i in range(t):
	game=True
	n=int(input())
	strn=input()
	arr=[]
	arr1=[]
	for i in range(len(strn)):
		if strn[i] in arr:
			if strn[i-1]==strn[i]:
				arr1.append(strn[i])
			else:
				print("NO")	
				game=False
				break
		else:
			arr.append(strn[i])
	if game==True:
		print("YES")
